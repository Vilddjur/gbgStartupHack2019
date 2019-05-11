#!/usr/bin/env python3

import flask
import json
import newspaper

from sental.sentimental_analyser import SentimentalAnalyser
from testing_stuff import mock
import newsfetch.news


app = flask.Flask(__name__)


def is_website_news_source(url):
    """
    Given a website, return if website is a news source.

    Return: bool
    """
    raise NotImplementedError


def get_related_articles(url):
    """
    Given a URL, return list of related articles

    Return: list[str]
    """
    return news.get_related_articles(url)


def parse_article(url):
    """
    Given a URL, return the article text

    Return: dict
    """
    article = newspaper.Article(url)
    article.download()
    article.parse()

    return {
        'authors': article.authors,
        'publishDate': article.publish_date,
        'text': article.text
    }


def get_sentiment(text):
    """
    Given text, return sentiments

    Arguments:
        text(str): string with article content

    Return:
        dict: 
            {
                'polarity': 'positive/neutral/negative',
                'subjectivity': 'subjective/objective',
                'text': 'analysed text',
                'polarity_confidence': 0.0 - 1.0,
                'subjectivity_confidence': 0.0 - 1.0
            }
    """
    sent_al = SentimentalAnalyser()
    sentiment = sent_al.get_sentiment(text)

    return sentiment



@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/coffee', methods=['POST'])
def coffee():
    """
    Production endpoint.
    """
    url = request.form.get('url')

    article = parse_article(url)
    sentiment = get_sentiment(article['text'])


@app.route('/api/beer', methods=['POST'])
def beer():
    """
    Mock endpoint. FOR TESTING.
    """
    return mock()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
