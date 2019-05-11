import requests

new_key='1b89d91f976447cb89c3310dda3143ec'
OK=200


def get_querystring(source_url):
    """
    Extract query information from article.
    """
    raise NotImplemented


def get_related_articles(source_url):
    """
    Returns a list of urls to related articles sorted by sentiment.
    """
    title = 'bitcoin'
    query = title
    req = ('https://newsapi.org/v2/everything?'
            'q='+query+'&'
            'apiKey='+new_key)

    print(req)
    res = requests.get(req)
    print("Response status %i" % res.status_code)

    urls = []
    if res.status_code == OK:
        json = res.json()
        articles = json['articles']
        print("Found %i articles." % len(articles))

        for article in articles:
            #print("URL: " % article['url'])
            urls.append(article['url'])

    for url in urls:
        #article = extract_article(url)
        #sentiment = sentiment(article)

    return urls


if __name__ == '__main__':
    print(get_related_articles('https://edition.cnn.com/2019/05/11/opinions/trump-tramples-world-intl/index.html'))
