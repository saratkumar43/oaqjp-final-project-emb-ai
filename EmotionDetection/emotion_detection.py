import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    emotion_d = formatted_response['emotionPredictions'][0]['emotion']
    anger_v = emotion_d['anger']
    disgust_v = emotion_d['disgust']
    fear_v = emotion_d['fear']
    joy_v = emotion_d['joy']
    sadness_v = emotion_d['sadness']

    domemotion = max(emotion_d, key=emotion_d.get)
    domemotion_v = emotion_d[domemotion]

    return {'anger': anger_v, 'disgust': disgust_v, 'fear': fear_v, 'joy': joy_v, 'sadness': sadness_v, 'dominant_emotion': domemotion} # Return the response text from the API