<h1>Topic Modeller</h1>


<h4>This is a standalone application which can be used to extract the relevant topics from a webpage.</h4>

<h2>Steps to Run</h2>

<p>Clone the repository and run the following commands inside the root directory</p>

```
pip3 install -r requirements.txt
python3 main.py
```

<h2>Endpoints</h2>

```
POST /topics
Request Body: {
  url: String
  num_topics: Integer(Optional,default value = 5)
}
Response Body: {
  topics: List
}
Example CURL:
curl -X POST "http://localhost:8000/topics" -H "Content-Type: application/json" -d '{"url":"http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/"}'
```

You can replace the url in above CURL with any url out of which you are looking to find the relevant topics.


<h2>Approach</h2>

We are using topic modeling to find out the relevant topics from a web page. It is a natural language processing (NLP) technique used to discover underlying topics or themes within a collection of text documents. It is a form of unsupervised machine learning where the algorithm identifies patterns in the text data to group words or phrases that are contextually related. The primary goal of topic modeling is to find the hidden thematic structure in the textual data, making it easier to understand, categorize, and analyze large sets of documents.

We are using Latent Dirichlet Allocation (LDA) which is one of the most popular and widely used topic modeling techniques. LDA is a generative probabilistic model that assumes each document is a mixture of a small number of topics, and each word in the document is attributable to one of the document's topics. LDA is based on two main concepts:

1. Topics: LDA assumes that documents are composed of a fixed number of topics. Topics represent the underlying themes or subject matters in the text data. Each topic is characterized by a distribution of words, and these words are often keywords or terms associated with the topic.

2. Latent Structure: LDA considers that the topic structure within a document and the distribution of words within topics are latent (hidden) variables. It infers these hidden structures based on the observed words in the documents.

LDA and topic modeling, in general, have a wide range of practical applications, including text mining, content analysis, information retrieval, and document summarization, among others. They are instrumental in making sense of large and unstructured text data, allowing users to explore, categorize, and extract valuable information from textual documents.


<h5>Libraries Used</h5>

```
Gensim - It is an open-source Python library designed for natural language processing and text analysis
BeautifulSoup - It is a Python library for web scraping and parsing HTML and XML documents
```
