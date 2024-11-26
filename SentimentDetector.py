from textblob import TextBlob as TB

def detect_sentiment(text):
    blob = TB(text)

    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0.0:
        sentiment_category = 'Positive'
    elif polarity < 0.0:
        sentiment_category = 'Negative'
    else:
        sentiment_category = 'Neutral'

    return sentiment_category
    # print(f'Your Sentiment is {polarity}')