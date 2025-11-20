from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import librosa
import os
import logging
import requests
from flask_cors import CORS

app = Flask(__name__)

# -------------------------
# ENABLE CORS FOR FRONTEND
# -------------------------
# Allow ALL origins for testing and Netlify/frontend
CORS(app, resources={r"/*": {"origins": "*"}})

# -------------------------
# LOGGING SETUP
# -------------------------
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/backend.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# -------------------------
# LOAD MODEL
# -------------------------
MODEL_PATH = 'distress_model.h5'

model = None
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    logging.info("✅ Model loaded successfully.")
else:
    logging.warning("⚠️ Model file not found! Put distress_model.h5 in the backend folder.")

# -------------------------
# ROUTES
# -------------------------
@app.route('/')
def home():
    return jsonify({'message': 'EmpowerHer Flask API is running!'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500

        # Correct field name expected from frontend
        if 'file' not in request.files:
            return jsonify({'error': 'No audio file uploaded. Expected field name: file'}), 400

        file = request.files['file']
        file.save('temp.wav')

        # Extract MFCC
        y, sr = librosa.load('temp.wav', duration=3, offset=0.5)
        mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)

        x = np.expand_dims(mfccs, axis=0)
        pred = model.predict(x)

        # Arya said: sigmoid output → distress if > 0.5
        confidence = float(pred[0][0])
        prediction = 'distress' if confidence > 0.5 else 'normal'

        logging.info(f"Prediction: {prediction} | Confidence: {confidence}")

        return jsonify({
            'prediction': prediction,
            'confidence': confidence
        })

    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/alert', methods=['POST'])
def alert():
    """
    This endpoint will send SNS alert (once Srushti sets AWS credentials / role).
    """
    try:
        return jsonify({'error': 'SNS credentials not configured'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
