# 💜 EmpowerHer – AI-Powered Women Safety System

EmpowerHer is an **AI + Cloud-based safety system** designed to detect distress or panic in a user’s voice and automatically trigger SOS alerts to trusted contacts or NGOs — without manual intervention.

## 🚀 Overview

The system listens for distress signals through voice tone analysis using an AI model trained on emotion datasets (RAVDESS, CREMA-D).  
Once distress is detected, the system triggers a **Twilio-powered SMS alert** via the **Flask backend** hosted on **AWS EC2**.

---

## 🧩 Components

| Module | Description | Contributor |
|--------|--------------|--------------|
| 🎨 Frontend | React UI with real-time interaction and visual alerts | **Sara Kolas** |
| 🧠 AI Model | CNN/LSTM trained on emotional voice data | **Arya Raut** |
| ⚙️ Backend | Flask API integration + model inference | **Shravani Khurpe** |
| ☁️ Cloud & Alerts | AWS EC2 deployment + Twilio SMS integration | **Srushti Aravandekar** |

---

## 💻 Tech Stack

- React.js (Frontend)
- Flask (Backend)
- TensorFlow / Keras (AI Model)
- AWS EC2 (Cloud Hosting)
- Twilio API (SMS Alerts)
- Firebase / MongoDB (Data Storage - optional)

---

## ⚙️ How It Works

1. 🎙️ The user speaks — voice is captured via mic.
2. 🧠 AI model analyzes the voice for distress emotions.
3. ☁️ Flask backend sends prediction results to the cloud.
4. 🚨 If distress detected → Twilio sends an SMS alert.

---

## 🪄 Setup Instructions

### 1. Clone this repo
```bash
git clone https://github.com/SaraKolas/EmpowerHer-Frontend.git
cd EmpowerHer-Frontend
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
