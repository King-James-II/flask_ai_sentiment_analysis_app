'''
Flask app for sentiment analysis on localhost:5000.
Endpoint "/sentimentAnalyzer" analyzes text input.
Uses sentiment_analyzer from SentimentAnalysis package.

'sent_analyzer' processes input, runs analysis, and returns results.
If no text provided, returns prompt; for invalid input, returns error.

Endpoint "/" renders main page with index.html.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = str(request.args.get('textToAnalyze').lower())
    if text_to_analyze == "":
        return "Please input text to analyze."
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input! Try again."
    return f"The given text was identified as {label.split('_')[1]} with a score of {score}"

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
