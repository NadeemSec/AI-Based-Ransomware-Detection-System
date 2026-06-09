from flask import Flask, render_template, jsonify, request
from monitor import start_monitoring
from predictor import predict_ransomware
import random

app = Flask(__name__)

# Dashboard Counters
scans = 0
threats = 0
suspicious = 0

# AI Status
ai_running = True


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_data')
def get_data():

    global scans, threats, suspicious, ai_running

    if not ai_running:
        return jsonify({
            "scans": scans,
            "threats": threats,
            "suspicious": suspicious,
            "latest_log": "AI Monitoring Stopped",
            "log_type": "warning",
            "ai_status": "STOPPED"
        })

    scans += random.randint(5, 15)

    activity, level = start_monitoring()

    if level == "danger":
        threats += 1

    elif level == "warning":
        suspicious += 1

    return jsonify({
        "scans": scans,
        "threats": threats,
        "suspicious": suspicious,
        "latest_log": activity,
        "log_type": level,
        "ai_status": "ACTIVE"
    })


@app.route('/toggle_ai', methods=['POST'])
def toggle_ai():

    global ai_running

    ai_running = not ai_running

    return jsonify({
        "status": "ACTIVE" if ai_running else "STOPPED"
    })


@app.route('/predict', methods=['POST'])
def predict():

    try:

        data = request.get_json()

        result = predict_ransomware(data)

        if result == 0:
            prediction = "NORMAL TRAFFIC"
            confidence = random.randint(90, 98)

        elif result == 1:
            prediction = "SUSPICIOUS ACTIVITY"
            confidence = random.randint(80, 90)

        else:
            prediction = "RANSOMWARE DETECTED"
            confidence = random.randint(92, 99)

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })

    except Exception as e:

        return jsonify({
            "prediction": f"Error: {str(e)}",
            "confidence": 0
        })


@app.route('/reset')
def reset():

    global scans, threats, suspicious

    scans = 0
    threats = 0
    suspicious = 0

    return jsonify({
        "message": "Dashboard Reset Complete"
    })


if __name__ == "__main__":
    app.run(debug=True)