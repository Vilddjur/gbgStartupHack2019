#!/usr/bin/env python3

import requests
import json
import logging

news_key='1b89d91f976447cb89c3310dda3143ec'
OK=200


def get_related_articles(source_url, log=False):
    """
    Given a URL, return list of related articles.

    Return: list[str]
    """
    def logprint(text):
        if log: print(text)

    title = 'bitcoin'
    query = title
    req = ('https://newsapi.org/v2/everything?'
            'q='+query+'&'
            'apiKey='+news_key)

    logprint(req)

    res = requests.get(req)
    logprint("Response status %i" % res.status_code)

    urls = []
    if res.status_code == OK:
        body = res.json()
        if log:
            with open('related_article_dump.json', 'w+') as out:
                json.dump(body, out, indent=4)

        articles = body['articles']
        logprint("Found %i articles." % len(articles))

        for article in articles:
            urls.append(article['url'])

    return urls


if __name__ == '__main__':
    get_related_articles('https://edition.cnn.com/2019/05/11/opinions/trump-tramples-world-intl/index.html')
