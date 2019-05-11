from .sentimental_analyser import SentimentalAnalyser

def main():
    sent_al = SentimentalAnalyser()
    sentiment = sent_al.get_sentiment('We are gonna win startuphack')
    print(sentiment)
    
    
    return 0


if __name__ == '__main__':
    main()
