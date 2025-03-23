from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector')
def emotion_predictor():

    text_to_analyze = requests.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    
    anger = response['anger']
    disgust = response['disgust']git remote -v1
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid input, try again"
    else:
        return "Response is 'anger':{}, 'disgust':{}, 'fear':{}, 'joy':{} and 'sadness':{}.\nDominant emotion is {}.".format(anger, disgust, fear, joy, sadness, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

