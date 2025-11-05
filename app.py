from flask import Flask, request, jsonify
import librosa
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('../distress_model.h5')

@app.route('/')
def home():
    return "EmpowerHer AI backend is running!"

@app.route('/predict', methods=['POST'])
def predict():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    y, sr = librosa.load(audio_file, sr=None)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    mfcc = np.expand_dims(mfcc, axis=0)

    prediction = model.predict(mfcc)
    label = 'distress' if prediction[0][0] > 0.5 else 'normal'

    return jsonify({'alert': label})

if __name__ == '__main__':
    app.run(debug=True)
