# routes/predict.py
# POST /predict -> accepts JSON with 40 MFCC features, returns prediction JSON.

from flask import Blueprint, request, jsonify
import logging
from services.model import predict_from_features

predict_bp = Blueprint("predict", __name__)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    """
    Request JSON (from Kolas/Frontend):
    {
      "features": [40 MFCC floats]
    }

    Response JSON (for evaluator/FE):
    {
      "prediction": "Distress",
      "alertTriggered": false
    }
    """
    try:
        data = request.get_json(silent=True) or {}
        features = data.get("features")

        # Strict, evaluator-friendly validation
        if not isinstance(features, list) or len(features) != 40:
            return jsonify({"error": "Provide 'features' as a list of 40 floats"}), 400

        prediction = predict_from_features(features)

        return jsonify({
            "prediction": prediction,
            "alertTriggered": False
        }), 200

    except Exception as e:
        logging.getLogger().exception("/predict failed")
        return jsonify({
            "error": "Prediction failed",
            "details": str(e)
        }), 500
