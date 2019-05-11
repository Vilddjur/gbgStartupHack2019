#!/usr/bin/env python3

import requests
import json
import logging
import sys

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

    req = ('https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/NewsSearchAPI?autoCorrect=true&pageNumber=1&pageSize=3&'
            'q='+'+'.join(query.split())+'&'
            'safeSearch=true')

    logprint(req)

    res = requests.get(req, 
              headers={
                "X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
                "X-RapidAPI-Key": "2281645066mshb5fe08876b82c2fp1b8045jsn816ee735b171"
              })
    logprint("Response status %i" % res.status_code)

    urls = {}
    if res.status_code == OK:
        body = res.json()
        if log:
            with open('related_article_dump.json', 'w+') as out:
                json.dump(body, out, indent=4)

        articles = body['value']
        logprint("Found %i articles." % len(articles))

        for article in articles:
            urls[article['url']] = article

    return urls


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Wrong number of arguments!\nUsage: ./news.py \'query_string\'")
        sys.exit(1)
    print(get_related_articles(sys.argv[1]))
