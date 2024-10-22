"""Module for Emotion Detection using Flask."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=['POST', 'GET'])
def emotion_detect():
    """Handle the emotion detection request."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Check if the response contains an error
    if 'error' in response:
        return response['error'], 400  # Return the error message with a 400 status code

    # Extract emotion scores
    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion')

    # Check if dominant_emotion is None
    if dominant_emotion is None:
        return "Invalid text! Please try again!", 400  # Return the error - 400 status code

    # Prepare the formatted response
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    """Render the main index page of the application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
