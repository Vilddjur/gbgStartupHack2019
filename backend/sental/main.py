import argparse
from .sentimental_analyser import SentimentalAnalyzer

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("api", help="IBM or aylien")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    sent_al = SentimentalAnalyzer(args.api)
    sentiment = sent_al.get_sentiment('We are gonna win startuphack')
    print(sentiment)
    
    
    return 0


if __name__ == '__main__':
    main()
