# routes/alert.py
# POST /alert -> triggers AWS SNS to notify contacts.

from flask import Blueprint, jsonify
import logging
import boto3
import os

alert_bp = Blueprint("alert", __name__)

@alert_bp.route("/alert", methods=["POST"])
def alert():
    """
    Response JSON:
    {
      "prediction": "Distress",
      "alertTriggered": true
    }
    """
    try:
        topic_arn = os.getenv("SNS_TOPIC_ARN")

        if not topic_arn:
            return jsonify({"error": "SNS_TOPIC_ARN not set"}), 500

        sns = boto3.client("sns", region_name=os.getenv("AWS_DEFAULT_REGION"))
        sns.publish(
            TopicArn=topic_arn,
            Message="🚨 Distress detected by EmpowerHer AI",
            Subject="Distress Alert"
        )

        return jsonify({
            "prediction": "Distress",
            "alertTriggered": True
        }), 200

    except Exception as e:
        logging.getLogger().exception("/alert failed")
        return jsonify({
            "error": "SNS alert failed",
            "details": str(e)
        }), 500
