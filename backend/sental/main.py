import os
import json
from aylienapiclient import textapi


class SentimentalAnalyser:
    def __init__(self):
        conf_path = os.path.join(os.path.dirname(__file__), 'conf.json')
        with open(conf_path) as f_h:
            conf = json.load(f_h)
        self.client = textapi.Client(conf['app_id'], conf['app_key'])

    def get_sentiment(self, text):
        return self.client.Sentiment({'text': text})


def main():
    sent_al = SentimentalAnalyser()
    sentiment = sent_al.get_sentiment('We are gonna win startuphack')
    print(sentiment)
    
    
    return 0


if __name__ == '__main__':
    main()
