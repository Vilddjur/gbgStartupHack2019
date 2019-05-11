import os
import json
from aylienapiclient import textapi
from ibm_watson import ToneAnalyzerV3


class UnsupportedAPIException(Exception):
    pass


class SentimentalAnalyzer:
    def __init__(self, api='IBM'):
        if api == 'IBM':
            self.sentimental_analyzer = IBMSentimentalAnalyzer()
        elif api == 'aylien':
            self.sentimental_analyzer = AylienSentimentalAnalyzer()
        else:
            raise UnsupportedAPIException('API must be IBM or aylien')

    def get_sentiment(self, text):
        return self.sentimental_analyzer.get_sentiment(text)


class AylienSentimentalAnalyzer(SentimentalAnalyzer):
    def __init__(self):
        conf_path = os.path.join(os.path.dirname(__file__), 'conf.json')
        with open(conf_path) as f_h:
            conf_file = json.load(f_h)
            api_conf= conf_file['aylien']
        self.client = textapi.Client(api_conf['app_id'], api_conf['apikey'])

    def get_sentiment(self, text):
        return self.client.Sentiment({'text': text})
    

class IBMSentimentalAnalyzer(SentimentalAnalyzer):
    def __init__(self):
        conf_path = os.path.join(os.path.dirname(__file__), 'conf.json')
        with open(conf_path) as f_h:
            conf_file = json.load(f_h)
            api_conf= conf_file['IBM']
        self.tone_analyzer = ToneAnalyzerV3(
                                version = '2017-09-21',
                                iam_apikey = api_conf['apikey'],
                                url = api_conf['endpoint'])

    def get_sentiment(self, text):
        tone_analysis = self.tone_analyzer.tone(
                                text,
                                content_type = 'text/plain',
                            ).get_result()
        return tone_analysis
