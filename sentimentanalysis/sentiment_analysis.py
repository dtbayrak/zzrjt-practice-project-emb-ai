
# Import the requests library to handle HTTP requests
import requests 
import json

# Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
def sentiment_analyzer(text_to_analyse): 
    
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' 

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } } 

    # Custom header specifying the model ID for the sentiment analysis service 
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 
    
    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json = myobj, headers=header) 

    # Parsing the JSON response and convert it into object (deserialize)
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response 
    label = formatted_response['documentSentiment']['label'] 
    score = formatted_response['documentSentiment']['score']

    # Returning a dictionary containing sentiment analysis results 
    return {'label': label, 'score': score}
