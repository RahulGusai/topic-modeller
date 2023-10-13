from bs4 import BeautifulSoup
import requests
import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.parsing.preprocessing import *


class HTMLParser(object):

    def get_html_from_url(self, url):
        try:
            response = requests.get(url)
            return response.content
        except Exception as e:
            pass
            # throw Exception here

    def parse_html(self, html_text):
        try:
            soup = BeautifulSoup(html_text, 'html.parser')
            return soup.get_text().lower()
        except Exception as e:
            pass
            # throw Exception here

    def find_topics_from_parsed_html(self, parsed_html, num_topics):
        try:
            STOPWORDS = ["a", "an", "the", "in", "at", "on", "of", "and", "to"]
            custom_filters = [lambda x: x.lower(), strip_tags,
                              strip_punctuation, remove_stopwords,
                              strip_multiple_whitespaces, strip_short]
            tokens = preprocess_string(parsed_html, filters=custom_filters)

            dictionary = corpora.Dictionary([tokens])
            corpus = [dictionary.doc2bow(tokens)]

            lda_model = LdaModel(
                corpus, num_topics=num_topics, id2word=dictionary)

            topics = lda_model.print_topics(num_words=5)
            all_words = []
            for topic in topics:
                probability_distribution_str = topic[1]
                current_topic_words = []
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
        except Exception as e:
            pass
