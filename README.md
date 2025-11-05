# 🎙️ EmpowerHer – AI Distress Detection Model

EmpowerHer is an **AI-powered women safety system** designed to detect distress in voice tone and automatically trigger alerts through a **cloud-based system**, without the user needing to manually send an SOS.

This repository contains the **AI module** of the EmpowerHer system — a machine learning model trained on emotional speech data to recognize signs of **fear, anger, and panic**, which represent distress situations.

---

## 🧠 Project Overview

The AI model analyzes short audio samples using **MFCC (Mel-frequency cepstral coefficients)** features and a **deep learning classifier (Keras/TensorFlow)** to detect distress tones in voice.

Although the project aims to help victims of domestic abuse, it uses the **RAVDESS Emotional Speech Audio Dataset**, which contains **acted emotional voices** (e.g., fear, anger, calm).  
This allows us to safely and ethically simulate distress detection for prototype development.

---

## 🧩 Features

- 🎤 **Voice Emotion Detection** using MFCC features  
- 🧠 **CNN/LSTM-based deep learning model**  
- ☁️ **Cloud Integration Ready (Flask + Twilio)**  
- ⚡ **Real-time distress detection and SMS alert trigger**  
- 🧱 **Modular design** – integrates easily with backend and UI

---

## 📂 Files in This Repository

| File | Description |
|------|--------------|
| `distress_model.h5` | Final trained AI model for distress detection |
| `test_predict.py` | Script to test model predictions on new audio files |
| `EmpowerHer_AI.ipynb` | Google Colab training notebook |
| `requirements.txt` | List of dependencies (TensorFlow, Librosa, etc.) |
| `README.md` | Project documentation file |

---

## 🚀 How to Use

1. **Clone this repository:**
   ```bash
   git clone https://github.com/aryarautt/EmpowerHer_AI.git
   cd EmpowerHer_AI
