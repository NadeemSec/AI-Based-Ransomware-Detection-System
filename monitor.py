import random
import os
from datetime import datetime

LOG_FILE = "logs/threat_logs.txt"

os.makedirs("logs", exist_ok=True)

activities = [
    ("Normal File Access", "safe"),
    ("File Scan Completed", "safe"),
    ("Network Traffic Analyzed", "safe"),
    ("Multiple File Rename Detected", "warning"),
    ("Unknown Process Accessing Files", "warning"),
    ("Suspicious Encryption Activity", "danger"),
    ("Ransomware Signature Detected", "danger"),
]

def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def start_monitoring():
    activity, level = random.choice(activities)
    write_log(activity)
    return activity, level