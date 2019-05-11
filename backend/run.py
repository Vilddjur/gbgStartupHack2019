#!/usr/bin/env python3

import flask
import json
import newspaper
from flask import request

from sental.sentimental_analyzer import SentimentalAnalyzer
from testing_stuff import mock
from newsfetch import news


app = flask.Flask(__name__)


def is_website_news_source(url):
    """
    Given a website, return if website is a news source.

    Return: bool
    """
    raise NotImplementedError


def get_related_articles(query):
    """
    Given a URL, return list of related articles

    Return: list[str]
    """
    return news.get_related_articles(query)


def parse_article(url):
    """
    Given a URL, return the article text

    Return: dict
    """
    article = newspaper.Article(url)
    article.download()
    article.parse()

    return {
        'title': article.title,
        'authors': article.authors,
        'publishDate': str(article.publish_date),
        'text': article.text,
        'url': url
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


def sort_sentiments(source, related_articles):
    """
    Return sorted urls for related articles based on how different sentiment is
    compared with source article.

    Args:
        source: Sentiment of 
    """
    for article in related_articles:
        pass
    return list(related_articles.keys())


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

    source_article = dict()
    related_articles = list()

    with open('articles_caching.json') as f_h:
        cached_articles = json.load(f_h)
    if url not in cached_articles:
        print('CACHE_MISS: {}'.format(url))
        source_article = parse_article(url)
        query = source_article['title']

        source_article.update({'related_articles': get_related_articles(query)})
        cached_articles.update({url: source_article})
        with open('articles_caching.json', 'w') as f_h:
            json.dump(cached_articles, f_h, indent=4)
    else:
        print('CACHE_HIT')
        source_article = cached_articles[url]

    source_sentiment = dict()
    if source_article['title'] not in cached_articles:
        source_sentiment = get_sentiment(source_article['text'])
        cached_articles.update({source_article['title']: source_sentiment})
    else:
        source_sentiment = cached_articles[source_article['title']]
            
    sentiments = dict()
    for related_url in source_article['related_articles']:
        article = dict()
        if related_url not in cached_articles:
            article = parse_article(related_url)
            query = article['title']

            article.update({'related_articles': get_related_articles(query)})
            cached_articles.update({related_url: article})
            with open('articles_caching.json', 'w') as f_h:
                json.dump(cached_articles, f_h, indent=4)
        else:
            article = cached_articles[related_url] 

        if article['title'] not in cached_articles:
            sentiments[related_url] = get_sentiment(article['text'])
            cached_articles.update({article['title']: sentiments[related_url]})
            with open('articles_caching.json', 'w') as f_h:
                json.dump(cached_articles, f_h, indent=4)
        else:
            sentiments[related_url] = cached_articles[article['title']]

    ranked_articles = sort_sentiments(source_sentiment, sentiments)
    return '\n'.join(ranked_articles)+'\n'


@app.route('/api/beer', methods=['POST'])
def beer():
    """
    Mock endpoint. FOR TESTING.
    """
    return mock()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
