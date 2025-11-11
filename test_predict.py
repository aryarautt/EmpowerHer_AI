import sys
import librosa
import numpy as np
import tensorflow as tf

# Load the trained model
model = tf.keras.models.load_model('distress_model.h5')

def predict_distress(file_path):
    y, sr = librosa.load(file_path, duration=3, offset=0.5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfccs = np.mean(mfcc.T, axis=0)
    x = np.expand_dims(mfccs, axis=0)
    pred = model.predict(x)
    label = np.argmax(pred, axis=1)[0]
    return 'distress' if label == 1 else 'normal'

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_predict.py <audio_file_path>")
    else:
        file_path = sys.argv[1]
        print("Prediction:", predict_distress(file_path))
