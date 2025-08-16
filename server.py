"""
Module Name: emotion_detection.py
Description: This module contains functions for emotion detection based on AI.
Author: Sarat Kumar
Date: 2025-08-15
"""

#  Python library for Flak modules
from flask import Flask, render_template, request

# Customized module for Emotion detector
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    '''
    Route Decorator to calculate emotion detection using IBM AI libraries
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a formatted string with the sentiment label and score
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {response['anger']}, "

@app.route("/")
def render_index_page():
    '''
    Route Decorator to calculate emotion detection using IBM AI libraries
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
