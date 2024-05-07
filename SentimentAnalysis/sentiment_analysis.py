"""
This module provides a function sentiment_analyzer that processes text using IBM's AI Watson.
It returns a dictionary for processing.
"""

import json
import requests

def sentiment_analyzer(text_to_analyze):
    """
    This function takes in text as an argument and processes it using sentiment analysis AI.
    It returns the label such as POSITIVE, NEGATIVE, or NEUTRAL as well as the score.
    1.0 being the highest positive and -1.0 being the highest negative. 0 is a neutral score.
    """

    # Define the URL for the sentiment analysis API
    url = ("https://sn-watson-sentiment-bert.labs.skills.network/"
           "v1/watson.runtime.nlp.v1/NlpService/SentimentPredict")

    # Prepare the request body with the text to be analyzed
    req_body = {"raw_document": {"text": text_to_analyze}}

    # Define the header with necessary metadata
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Send a POST request to the sentiment analysis API
    response = requests.post(url, json=req_body, headers=header, timeout=10)

    # Parse the JSON response
    formatted_response = json.loads(response.text)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        # Handle server error by setting label and score to None
        label = None
        score = None

    # Return the result as a dictionary
    return {"label": label, "score": score}
    