#!/usr/bin/env python3

import flask
import json

from sental.sentimental_analyser import SentimentalAnalyser


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
    raise NotImplementedError


def get_article_text(url):
    """
    Given a URL, return the article text

    Return: str
    """
    raise NotImplementedError


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


def mock():
    tone = {
        'anger': 0.55,
        'fear': 0.0,
        'joy': 0.6,
        'sadness': 0.1,
        'analytical': 0.42,
        'confident': 0.0,
        'tentative': 0.7,
    }

    article1 = {
        'source': 'TechCrunch',
        'title': 'India’s most popular services are becoming super apps',
        'url': 'https://techcrunch.com/2019/05/10/india-super-apps/',
        'tone': tone,
    }

    article2 = {
        'source': 'BBC',
        'title': ('US sends Patriot missile system to Middle East amid Iran '
                  'tensions'),
        'url': 'https://www.bbc.com/news/world-us-canada-48235940',
        'tone': tone,
    }

    article3 = {
        'source': 'Guardian',
        'title': ('Nearly all countries agree to stem flow of plastic waste '
                  'into poor nations'),
        'url': ('https://www.theguardian.com/environment/2019/may/10/nearly-al'
                'l-the-worlds-countries-sign-plastic-waste-deal-except-us'),
        'tone': tone,
    }

    response = {
        'currentArticle': article3,
        'relatedArticles': [article1, article2],
    }

    return json.dumps(response)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/api/beer', methods=['POST'])
def beer():
    return mock()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
