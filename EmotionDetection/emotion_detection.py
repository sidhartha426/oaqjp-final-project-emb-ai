import requests,json

def format_output(data):
    dominant_value = data['joy']
    doimnat_emotion = 'joy'
    for emotion, value in data.items():
        if value > dominant_value:
            dominant_value = value
            doimnat_emotion = emotion
    data['dominant_emotion'] = doimnat_emotion
    return data


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,'dominant_emotion': None }
    formatted_response = json.loads(response.text)
    result = format_output(formatted_response["emotionPredictions"][0]["emotion"].copy())
    return result