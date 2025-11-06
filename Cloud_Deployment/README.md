# EmpowerHer – Cloud Deployment Documentation
**Contributor:** Srushti Aravandekar  
**Role:** Cloud Engineer  

---

## Overview
This document explains how the **EmpowerHer AI system** was deployed on AWS and connected to the AI model.  
The goal was to make the application accessible online and to enable real-time safety alerts through AWS services.

---

## Cloud Setup Summary

### 1. EC2 Instance (Backend Hosting)

| Configuration | Details |
|:--------------|:---------|
| **Service used** | Amazon EC2 |
| **Instance type** | t2.micro (Free Tier) |
| **Operating system** | Ubuntu Server 22.04 LTS |
| **Ports opened** | 22 – SSH <br> 80 – HTTP <br> 5000 – Flask application access |
| **Key file** | `empowerher.pem` (converted to `.ppk` for PuTTY) |

After connecting through PuTTY, prepare the environment:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
git clone https://github.com/aryarautt/EmpowerHer_AI.git
cd EmpowerHer_AI
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
nohup python3 app.py > empowerher.log 2>&1 &
This keeps the Flask server running continuously even after closing the SSH session.
```
### 2. AWS SNS (Alert Notifications)
An SNS topic named empowerher-alerts was created to send SMS notifications whenever the model predicts “Distress”.

| Parameter       | Description                                                    |
| :-------------- | :------------------------------------------------------------- |
| **Protocol**    | SMS                                                            |
| **Test Number** | Verified using AWS Console                                     |
| **Result**      | Successfully received a test message through Lambda publishing |

Example Lambda Test Code
```
const AWS = require('aws-sdk');
const sns = new AWS.SNS();

exports.handler = async () => {
  const params = {
    Message: 'Test alert from EmpowerHer',
    TopicArn: 'arn:aws:sns:us-east-1:XXXXXXXXXXXX:empowerher-alerts'
  };
  await sns.publish(params).promise();
  return { statusCode: 200, body: 'Alert sent' };
};
```

### 3. Flask Integration with SNS
The Flask app running on EC2 connects to SNS using boto3.
Whenever distress is detected, an SMS alert is automatically sent.

Flask Route Example
```
@app.route('/alert', methods=['POST'])
def alert():
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:XXXXXXXXXXXX:empowerher-alerts',
        Message='Distress detected! Immediate attention required.'
    )
    return jsonify({'status': 'Alert sent successfully'})
```
| Endpoint   | Purpose             |
| :--------- | :------------------ |
| `/predict` | AI model prediction |
| `/alert`   | Sends SMS alert     |

### 4. IAM Configuration and Security
| Setting                       | Description                                                          |
| :---------------------------- | :------------------------------------------------------------------- |
| **IAM User**                  | `empowerher-admin`                                                   |
| **Initial Access Policy**     | AdministratorAccess                                                  |
| **Final Restricted Policies** | AmazonEC2FullAccess <br> AmazonSNSFullAccess <br> AmazonS3FullAccess |
| **Key Management**            | Stored securely (not hard-coded in codebase)                         |
| **Flask Port 5000**           | Opened temporarily for testing, then restricted for security         |

All IAM permissions were scoped down to follow the principle of least privilege.

### System Architecture
```text
[ USER / VICTIM ]
        │
        ▼
[ FRONTEND (Kolas) ]
  → Web Interface (React/HTML)
        │
        ▼
[ BACKEND (Khurpe) ]
  → Flask API hosted on AWS EC2
        │
        ▼
[ AI MODEL (Arya) ]
  → Detects distress in voice/audio
        │
        ▼
[ CLOUD SERVICES (Srushti) ]
  → AWS SNS sends SMS alert
        │
        ▼
[ EMERGENCY CONTACT / AUTHORITY ]
```
### Outcome
| Component           | Result                                         |
| :------------------ | :--------------------------------------------- |
| Flask Backend       | Hosted successfully on AWS EC2                 |
| SNS Alerts          | Verified through real SMS messages             |
| AI Integration      | Real-time prediction achieved                  |
| Cloud Communication | Fully operational between AI, backend, and AWS |
| System Stability    | Continuous operation confirmed                 |

Final Result: Complete AI-Cloud integration successfully achieved 🚀

### Key Learnings

* Hands-on experience with AWS EC2 instance setup and deployment.

* Deep understanding of IAM user roles and permission management.

* Integration of AI models with cloud-based services using APIs.

* Securely running and managing Flask applications in a production-like environment.

* Use of boto3 for server-to-cloud communication.n.

### Suggested Screenshots
Upload the following screenshots to the /Cloud_Deployment/screenshots/ folder:

| No. | Description           | File Name         |
| :-: | :-------------------- | :---------------- |
|  1  | EC2 instance running  | ec2-instance.png  |
|  2  | Flask terminal logs   | flask-running.png |
|  3  | SMS alert screenshot  | sns-alert.png     |
|  4  | AWS SNS topic console | sns-console.png   |

### Current Status
| Item           | Status     |
| :------------- | :--------- |
| EC2 Instance   | Running    |
| Flask Backend  | Deployed   |
| AI Integration | Working    |
| SNS Alerts     | Functional |
| Cloud Setup    | Completed  |

### Future Scope

* Integrate Twilio API for multi-region emergency calls.

* Build a user-friendly frontend with live voice capture.

* Migrate Flask app to AWS Lambda + API Gateway for serverless architecture.

* Add data storage in S3 for retraining AI models.

* Enable emotion detection (anger, fear, distress) to improve accuracy.
