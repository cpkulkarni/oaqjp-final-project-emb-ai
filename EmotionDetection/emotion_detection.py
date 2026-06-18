import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyze Emotion of the given text using Watson NLP BERT Emotion Analysis.
    Args:
        text_to_analyse (str): The text to be analyzed for Emotion
    Returns:
        response as text    """
    # Watson NLP API endpoint for Emotion analysis
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Request payload with the text to analyze
    payload = { "raw_document": { "text": text_to_analyze } }
    
    #try:
        # Make POST request to Watson NLP API
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 400:
                emotions = json.loads('{"anger": "None", "disgust": "None", "fear": "None", "joy": "None", "sadness": "None", "dominant_emotion": "None"}')
                return emotions


    # Parse the response
    if response.status_code == 200:
        print(response.text)
        response_data = response.text
        response_data = json.loads(response_data)
        emotions = response_data["emotionPredictions"][0]["emotion"]
        highest_emotion, highest_value = max(emotions.items(),  key=lambda item: item[1])            

        emotions["dominant_emotion"] = highest_emotion

        return emotions

        

    #except Exception as e:
    #    response = requests.post(url, json=payload, headers=headers)
    #    return response 
    #    return {
    #        'label': None,
    #        'score': None,
    #        'error': f'Unexpected error: {str(e)}'
    #    }  


