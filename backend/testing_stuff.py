import json

def news_to_html(news):
    ret ="<ul class='news-results'>"
    for art in news["relatedArticles"]:
        ret += "<li class='single-news-item'>"
        ret += "<article class='media'>"
        ret += "<figure class='media-left'>"
        ret += "<img class='news-image' src='" + currentArticle["urlToImage"] + "' />"
        ret += "</figure>"
        ret += "<div class='media-content'>"
        ret += "<div class='content'>"
        ret += "<h3 class='news-title'><a href='"+art["url"]+"'>" + art["title"] + "</a></h3>"
        ret += "</div>"
        ret += "</div>"
        ret += "</article>"
        #TODO: add tones
        ret += "</li>"
    ret += "</ul>"
    return ret

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
        'urlToImage': ('https://techcrunch.com/wp-content/uploads/2019/05/'
                       'GettyImages-880877228.jpg'),
        'tone': tone,
    }

    article2 = {
        'source': 'BBC',
        'title': ('US sends Patriot missile system to Middle East amid Iran '
                  'tensions'),
        'url': 'https://www.bbc.com/news/world-us-canada-48235940',
        'urlToImage': ('https://ichef.bbci.co.uk/news/660/cpsprodpb/E7B9/'
                       'production/_106912395_gettyimages-961853826.jpg'),
        'tone': tone,
    }

    article3 = {
        'source': 'Guardian',
        'title': ('Nearly all countries agree to stem flow of plastic waste '
                  'into poor nations'),
        'url': ('https://www.theguardian.com/environment/2019/may/10/nearly-al'
                'l-the-worlds-countries-sign-plastic-waste-deal-except-us'),
        'urlToImage': ('https://i.guim.co.uk/img/media/5ef7ee398fd5550c55764'
                       '628538b102ce316f194/0_0_3500_2100/master/3500.jpg'),
        'tone': tone,
    }

    response = {
        'currentArticle': article3,
        'relatedArticles': [article1, article2],
    }

    return news_to_html(response)
