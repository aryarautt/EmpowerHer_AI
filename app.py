from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import librosa
import os
import logging
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Allow frontend to call backend

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

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    logging.info("✅ Model loaded successfully.")
else:
    model = None
    logging.warning("⚠️ Model file not found! Please add 'distress_model.h5' to the project folder.")

# -------------------------
# ROUTES
# -------------------------
@app.route('/')
def home():
    return jsonify({'message': 'EmpowerHer Flask API is running!'})

# -------------------------
# PREDICT ENDPOINT
# -------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500

        if 'file' not in request.files:
            return jsonify({'error': 'No
