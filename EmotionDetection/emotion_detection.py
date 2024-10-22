import requests
import json

def emotion_detector(text_to_analyze):

    if not text_to_analyze.strip():
        return {
           'error': 'Invalid text! Please try again!'
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send the request to the API
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {
           'error': 'Invalid text! Please try again!'
        }
        
    # Convert the response to a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the required emotions and their scores
    emotions = formatted_response.get('emotion', {})
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Determine the dominant emotion
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Prepare the final output format
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result