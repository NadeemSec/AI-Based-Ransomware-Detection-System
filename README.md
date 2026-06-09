# AI-Based-Ransomware-Detection-System
AI-Based Ransomware Detection System using Machine Learning and Flask. This project uses a Random Forest Classifier to detect and classify ransomware-related activities as Safe, Suspicious, or Attack. Includes a real-time monitoring dashboard, threat prediction module, activity logs, and graphical visualization of security events.



# AI-Based Ransomware Detection System

This project is a Machine Learning-based cybersecurity solution designed to detect ransomware-related activities. The system uses a Random Forest Classifier trained on ransomware datasets and provides predictions through an interactive Flask web dashboard.

## Features

- Ransomware threat prediction
- Random Forest Machine Learning model
- Real-time monitoring simulation
- Threat logs and alerts
- Interactive dashboard
- Threat visualization using charts
- Flask web application

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- HTML
- CSS
- JavaScript
- Chart.js

## Machine Learning Model

Algorithm: Random Forest Classifier

Dataset Classes:
- SS = Safe
- S = Suspicious
- A = Attack

Model Accuracy:
- 99.39%

## Project Structure

AI_Ransomware_Detection_System/
│
├── app.py
├── predictor.py
├── monitor.py
├── train_model.py
│
├── model/
│   ├── ransomware_model.pkl
│   └── encoders.pkl
│
├── dataset/
│   └── final(2).csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

## Future Improvements

- User Authentication
- Database Integration
- Email Alerts
- Cloud Deployment
- Live Network Monitoring
- Deep Learning Models

## Authors
- Muhammad Nadeem

Supervisor:
- Sir Yawar Jan
