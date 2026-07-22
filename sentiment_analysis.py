import requests

def sentiment_analyzer(text_to_analyse) :
    
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict' 

    # Create a dictionary with the text to be analyzed
    obj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"} 

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = obj, headers=header) 

    # Return the response text from the API
    return response.text
