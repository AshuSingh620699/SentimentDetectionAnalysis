from flask import Flask, render_template, request
from SentimentDetector import detect_sentiment
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    senti = None
    if request.method == 'POST':
        txt = request.form['text']
        senti = detect_sentiment(txt)

    return render_template('index.html', sentiment=senti)

if __name__ == '__main__':
    app.run(debug=True)