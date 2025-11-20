from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import librosa
import os
import logging
import requests
from flask_cors import CORS

app = Flask(__name__)

# ------------------------------------
# FINAL CORS CONFIG (As Kolas required)
# ------------------------------------
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

# -------------------------
# LOGGING SETUP
# -------------------------
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/backend.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)": "%(message)s"
)

# -------------------------
# LOAD MODEL
# -------------------------
MODEL_PATH = "distress_model.h5"

model = None
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    logging.info("Model loaded successfully.")
else:
    logging.warning("Model file not found! Please upload distress_model.h5.")

# -------------------------
# ROUTES
# -------------------------
@app.route("/")
def home():
    return jsonify({"status": "EmpowerHer Flask API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None:
            return jsonify({"error": "Model not loaded"}), 500

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded. Expected field name: file"}), 400

        audio_file = request.files["file"]
        audio_file.save("temp.wav")

        # Load audio and extract MFCC
        y, sr = librosa.load("temp.wav", duration=3, offset=0.5)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfcc_mean = np.mean(mfcc.T, axis=0)

        x = np.expand_dims(mfcc_mean, axis=0)

        # Sigmoid output handling (Arya's model)
        pred = model.predict(x)
        confidence = float(pred[0][0])
        prediction = "distress" if confidence > 0.5 else "normal"

        logging.info(f"Prediction: {prediction}, Confidence: {confidence}")

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })

    except Exception as e:
        logging.error(f"Prediction failed: {str(e)}")
        return jsonify({"error": str(e)}), 500


@app.route("/alert", methods=["POST"])
def alert():
    """
    SNS / SMS alert will be handled once Srushti configures credentials or an instance role.
    """
    return jsonify({"error": "SNS not configured yet"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
