#!/usr/bin/env python3

import flask
import json
import newspaper

from sental.sentimental_analyzer import SentimentalAnalyzer
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
        api(str): Which api to use IBM/aylien,
                    WARNING: changes dictionary structure

    Return:
        {
            'IBM' {
                'tones': [{
                    'score': 0.673332,
                    'tone_id': 'joy',
                    'tone_name': 'Joy'
                }]
            }
            'aylien': {
                'polarity': 'positive/neutral/negative',
                'subjectivity': 'subjective/objective',
                'text': 'analysed text',
                'polarity_confidence': 0.0 - 1.0,
                'subjectivity_confidence': 0.0 - 1.0
            }
        }
    """
    ibm_sent_al = SentimentalAnalyzer('IBM')
    ibm_sentiment = ibm_sent_al.get_sentiment(text)
    aylien_sent_al = SentimentalAnalyzer('aylien')
    aylien_sentiment = aylien_sent_al.get_sentiment(text)
    return {'IBM': ibm_sentiment, 'aylien': aylien_sentiment}



@app.route('/')
def index():
    return 'Hello world'


@app.route('/test_sentimental')
def test_sentimental():
    with open('article.txt') as f_h:
        text = f_h.read()
    return str(json.dumps(get_sentiment(text), indent=4))

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
