import requests
import json 

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj ={ "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  

    formatted_response = json.loads(response.text)
    
    score = {}
    if response.status_code == 400:
        score = {'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None}
        return score 

    score = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant_emotion = max(score, key=score.get)
    
    score['dominant_emotion'] = dominant_emotion

    return score  
