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
