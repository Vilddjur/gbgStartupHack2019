#!/usr/bin/env python3

import requests
import json
import logging

news_key='1b89d91f976447cb89c3310dda3143ec'
OK=200

def news_to_html(news):
    ret ="<ul class='news-results'>"
    for art in news["relatedArticles"]:
        ret +="<li class='single-news-item'>"
        ret += "<img class='news-image' src='"+ art["urlToImage"] + "' />"
        ret += "<h3 class='news-title'><a href='"+art["url"]+"'>" + art["title"] + "</a></h3>"
        #TODO: add tones
        ret += "</li>"
    ret += "</ul>"
    return ret

def get_related_articles(query, log=False):
    """
    Given a URL, return list of related articles.

    Return: list[str]
    """
    def logprint(text):
        if log: print(text)

    req = ('https://newsapi.org/v2/everything?'
            'q='+query+'&'
            'apiKey='+news_key)

    logprint(req)

    res = requests.get(req)
    logprint("Response status %i" % res.status_code)

    urls = {}
    if res.status_code == OK:
        body = res.json()
        if log:
            with open('related_article_dump.json', 'w+') as out:
                json.dump(body, out, indent=4)

        articles = body['articles']
        logprint("Found %i articles." % len(articles))

        for article in articles:
            urls[article['url']] = article

    return urls


if __name__ == '__main__':
    get_related_articles('https://edition.cnn.com/2019/05/11/opinions/trump-tramples-world-intl/index.html')
