#!/usr/bin/env python3

import requests
import json
import logging
import pdb

news_key='1b89d91f976447cb89c3310dda3143ec'
OK=200


def get_related_articles(query, log=False):
    """
    Given a URL, return list of related articles.

    Return: list[str]
    """
    def logprint(text):
        if log: print(text)

    req = ('https://newsapi.org/v2/everything?'
            'q='+'+'.join(query.split())+'&'
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
    print(get_related_articles('Trump tramples and divides world, just like he does at home'))
    print(get_related_articles('Trump tariffs'))
