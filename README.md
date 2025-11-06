---



\# 🎙️ EmpowerHer – Backend (Flask API)



This is the \*\*Backend API for EmpowerHer\*\*, responsible for running the trained AI model, detecting distress from audio features, and triggering AWS SNS alerts in emergencies.

It is designed to be clean, modular, and easy to integrate with the frontend + EC2 deployment.



---



\# ✅ Features



\### 🔍 \*\*1. Emotion/Distress Prediction\*\*



\* Accepts \*\*40 MFCC features\*\*

\* Loads a trained \*\*TensorFlow/Keras model (distress\_model.h5)\*\*

\* Returns a JSON response:



```json

{

&nbsp; "prediction": "Distress",

&nbsp; "alertTriggered": true

}

```



\### 🚨 \*\*2. Emergency Alert via AWS SNS\*\*



\* Sends an alert notification using AWS SNS

\* Triggered manually through `/alert`

\* Uses environment variables for AWS credentials



\### ❤️ \*\*3. Health Check Endpoint\*\*



\* Simple GET endpoint for monitoring:



```json

{

&nbsp; "status": "Server is running"

}

```



\### 📁 \*\*4. Clean Backend Structure\*\*



\* `app.py` = Main Flask server

\* `routes/` = Modular routing (predict + alert)

\* `distress\_model.h5` = Trained AI model

\* Logging + error handling included



---



\# 📁 Folder Structure



```

backend/

│── app.py

│── distress\_model.h5

│── requirements.txt (if added)

│── routes/

│     ├── predict\_route.py

│     ├── alert\_route.py

│── utils/ (if used)

```



---



\# 🚀 API Endpoints



\## ✅ 1. Health Check



\*\*GET\*\* `/health`



\*\*Response\*\*



```json

{

&nbsp; "status": "Server is running"

}

```



---



\## ✅ 2. Predict Distress



\*\*POST\*\* `/predict`



\### Request Body:



```json

{

&nbsp; "features": \[40 MFCC feature values]

}

```



\### Response:



```json

{

&nbsp; "prediction": "Normal",

&nbsp; "alertTriggered": false

}

```



OR



```json

{

&nbsp; "prediction": "Distress",

&nbsp; "alertTriggered": true

}

```



---



\## ✅ 3. Trigger Emergency Alert



\*\*POST\*\* `/alert`



\### Response:



```json

{

&nbsp; "message": "Alert sent",

&nbsp; "alertTriggered": true

}

```



If SNS fails:



```json

{

&nbsp; "error": "SNS alert failed",

&nbsp; "details": "AWS error message"

}

```



---



\# 🔑 Environment Variables (Required)



Set these before running the server:



```

$env:SNS\_TOPIC\_ARN = "arn:aws:sns:REGION:ACCOUNT\_ID:topic"

$env:AWS\_ACCESS\_KEY\_ID = "YOUR\_KEY"

$env:AWS\_SECRET\_ACCESS\_KEY = "YOUR\_SECRET"

$env:AWS\_DEFAULT\_REGION = "us-east-1"

```



---



\# ▶️ Running the Backend (Local)



Install dependencies:



```

pip install -r requirements.txt

```



Run the server:



```

python app.py

```



Server will start at:



```

http://127.0.0.1:5000

```



---



\# 🧪 Testing the Backend (Examples)



\### ✅ Health Check



```

Invoke-RestMethod -Method Get -Uri "http://127.0.0.1:5000/health"

```



\### ✅ Predict



```

$features = @(0.01,0.02,...,0.40)

$body = @{ features = $features } | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5000/predict" -Body $body -ContentType "application/json"

```



\### ✅ Alert



```

Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:5000/alert"

```



---



\# 🏗️ Deployment Notes (EC2 / Frontend)



Frontend should call:



```

POST /predict

POST /alert

GET /health

```



Backend must run behind a \*\*security group that allows frontend traffic\*\*.



---



