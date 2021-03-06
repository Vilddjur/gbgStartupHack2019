#!/usr/bin/env python3

import flask
import json
import newspaper
import jinja2

from flask import request, abort
from sental.sentimental_analyzer import SentimentalAnalyzer
from testing_stuff import mock
from newsfetch import news

ARTICLES_CACHE='articles_caching.json'


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
    #(score, article)
    for article in related_articles:
        score = 0
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
    templ = jinja2.Template(open('template.j', 'r').read())
    url = request.form.get('url', None)

    if not url:
        abort(400)

    source_article = dict()
    related_articles = list()
   
    try:
        with open(ARTICLES_CACHE, 'r') as articles:
            pass
    except Exception:
        with open(ARTICLES_CACHE, 'w+') as f_h:
            f_h.write('{}\n')

    # Fetch article from cache or web.
    with open(ARTICLES_CACHE) as f_h:
        cached_articles = json.load(f_h)
    if url not in cached_articles:
        print('ARTICLE_CACHE_MISS: {}'.format(url))
        source_article = parse_article(url)
        query = source_article['title']

        source_article.update({'related_articles': get_related_articles(query)})
        cached_articles.update({url: source_article})
        with open(ARTICLES_CACHE, 'w') as f_h:
            json.dump(cached_articles, f_h, indent=4)
    else:
        print('ARTICLE_CACHE_HIT: {}'.format(url))
        source_article = cached_articles[url]

    # Fetch article sentiment from cache or web.
    source_sentiment = dict()
    if source_article['title'] not in cached_articles:
        print('SENTIMENT_CACHE_MISS: {}'.format(source_article['title']))
        source_sentiment = get_sentiment(source_article['text'])
        cached_articles.update({source_article['title']: source_sentiment})
    else:
        print('SENTIMENT_CACHE_HIT: {}'.format(source_article['title']))
        source_sentiment = cached_articles[source_article['title']]

    # Pair sentiment and articles?
    sentiments = dict()
    missing = [] # Not sure why it doesn't work without this but...
    for related_url in source_article['related_articles']:
        if related_url == url:
            missing.append(related_url)
            continue
        article = dict()

        # Update cache.
        if related_url not in cached_articles:
            print('ARTICLE_CACHE_MISS: {}'.format(related_url))
            try:
                article = parse_article(related_url)
            except Exception:
                print("ARTICLE PARSING FAILURE")
                missing.append(related_url)
                continue
            query = article['title']

            #article.update({'related_articles': get_related_articles(query)})
            cached_articles.update({related_url: article})
            with open(ARTICLES_CACHE, 'w') as f_h:
                json.dump(cached_articles, f_h, indent=4)
        else:
            print('ARTICLE_CACHE_HIT: {}'.format(related_url))
            article = cached_articles[related_url]

        # Remove 404 articles.
        if related_url in missing:
            continue;
        
        if article['title'] not in cached_articles and article['text'] != None:
            print('SENTIMENT_CACHE_MISS: {}'.format(article['title']))
            sentiments[related_url] = get_sentiment(article['text'])
            cached_articles.update({article['title']: sentiments[related_url]})
            with open('articles_caching.json', 'w') as f_h:
                json.dump(cached_articles, f_h, indent=4)
        else:
            print('SENTIMENT_CACHE_HIT: {}'.format(article['title']))
            sentiments[related_url] = cached_articles[article['title']]

    ranked_articles = sort_sentiments(source_sentiment, sentiments)
    rank_related_arts = []
    for art in ranked_articles:
        source_article['related_articles'][art]['tones'] = sentiments[art]['IBM']
        rank_related_arts.append(source_article['related_articles'][art])
    ret = {
        "currentArticle" : "",
        "relatedArticles": rank_related_arts
    }

    template_sentiments = dict()
    for item in source_sentiment['IBM']:
        template_sentiments[item['tone_name']] = item['score']

    return templ.render(
        template_sentiments=template_sentiments,
        template_articles=rank_related_arts,
        polarity=source_sentiment['aylien']['polarity'],
        subjectivity=source_sentiment['aylien']['subjectivity']
    )

    #return news.news_to_html(ret)


@app.route('/api/beer', methods=['POST'])
def beer():
    """
    Mock endpoint. FOR TESTING.
    """
    return mock()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
