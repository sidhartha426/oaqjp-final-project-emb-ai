''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function. The output returned shows the label and its emotions 
        score for the provided text.
    '''

    text_to_analyse = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyse)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return 'Invalid text! Please try again!.'

    result_string_1 = f'For the given statement, the system response is \'anger\': {anger}, '
    result_string_2 = f'\'disgust\': {disgust}, \'fear\': {fear}, \'joy\': {joy} '
    result_string_3 = f'and \'sadness\': {sadness}. The dominant emotion is {dominant_emotion}.'

    return result_string_1 + result_string_2 + result_string_3


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
