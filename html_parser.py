from bs4 import BeautifulSoup
import requests
from fastapi import HTTPException
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import *


class HTMLParser(object):
    def __init__(self, num_words=5):
        self.num_words = num_words

    def get_html_from_url(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail={"message": "Failed to fetch source of the requested url.", "exception": response.text})
        return response.content

    def parse_html(self, html_text):
        try:
            soup = BeautifulSoup(html_text, 'html.parser')
            return soup.get_text().lower()
        except Exception as e:
            raise HTTPException(
                status_code=500, detail={"message": "Failed to parse source of the requested url.", "exception": str(e)})

    def find_topics_from_parsed_html(self, parsed_html, num_topics):
        try:
            tokens = self.generate_tokens(parsed_html)
            dictionary = corpora.Dictionary([tokens])
            corpus = [dictionary.doc2bow(tokens)]

            lda_model = LdaModel(
                corpus, num_topics=num_topics, id2word=dictionary)
            topics = lda_model.print_topics(num_words=self.num_words)

            return self.extract_words_with_highest_probability(topics, num_topics)
        except Exception as e:
            raise HTTPException(status_code=500, detail={"message": "Failed to find topics from the parsed source of the requested url.",
                                "exception": str(e)})

    def generate_tokens(self, parsed_html):
        STOPWORDS = ["a", "an", "the", "in", "at", "on", "of", "and", "to"]
        custom_filters = [lambda x: x.lower(), strip_tags,
                          strip_punctuation, remove_stopwords,
                          strip_multiple_whitespaces, strip_short]
        return preprocess_string(parsed_html, filters=custom_filters)

    def extract_words_with_highest_probability(self, topics, num_topics):
        all_words = []
        for topic in topics:
            print(topic)
            current_topic_words = []
            probability_distribution_str = topic[1]
            probability_distribution_list = probability_distribution_str.split(
                '+')
            for probability_distribution in probability_distribution_list:
                new_word = probability_distribution.split('*')[1].strip()
                new_word = new_word.replace('"', "")
                current_topic_words.append(new_word)

            all_words.append(current_topic_words)

        result = set()
        for topic_words in all_words:
            for word in topic_words:
                if word not in result:
                    result.add(word)
                    break
            if len(result) == num_topics:
                return {'topics': list(result)}

        return {'topics': list(result)}
