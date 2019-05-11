import argparse
import json
from .sentimental_analyzer import SentimentalAnalyzer

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("api", help="IBM or aylien")
    parser.add_argument('--input-file', help="path to input file to analyze")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    text = 'We are gonna win startuphack' 
    if args.input_file:
        with open(args.input_file) as f_h:
            text = f_h.read() 
    sent_al = SentimentalAnalyzer(args.api)
    sentiment = sent_al.get_sentiment(text)
    print(json.dumps(sentiment, indent=4))
    
    
    return 0


if __name__ == '__main__':
    main()
