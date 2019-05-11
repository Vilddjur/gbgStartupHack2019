import flask
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



@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
