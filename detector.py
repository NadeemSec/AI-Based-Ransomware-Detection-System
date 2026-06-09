import joblib
import numpy as np

# Load trained model
model = joblib.load("model/ransomware_detector.pkl")

def detect_ransomware(features):

    try:
        features_array = np.array(features).reshape(1, -1)

        prediction = model.predict(features_array)[0]

        probability = model.predict_proba(features_array).max() * 100

        return prediction, round(probability, 2)

    except Exception as e:

        print("Detection Error:", e)

        return "Unknown", 0