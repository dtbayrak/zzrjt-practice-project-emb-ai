''' NLP sentiment analysis is the practice of using computers to recognize 
    sentiment or emotion expressed in a text. Through NLP, sentiment analysis 
    categorizes words as positive, negative or neutral. '''

import json
import requests

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse):
    ''' For creating the sentiment analysis application, we'll be making use of 
    the Watson Embedded AI Libraries. Since the functions of these libraries are 
    already deployed on the Cloud IDE server, there is no need of importing these 
    libraries to our code. Instead, we need to send a POST request to the relevant model 
    with the required text and the model will send the appropriate response.  '''

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Define the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Make a POST request to the sentiment analysis API with the first payload and headers
    response = requests.post(url, json = myobj, headers=header, timeout=(5, 10))

    if response.status_code == 200:
        # Parsing the JSON response and convert it into object (deserialize)
        formatted_response = json.loads(response.text)
        # Extracting sentiment label and score from the response
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = f'An error occurred with the HTTP status code: {response.status_code}'
        score = None
    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}
