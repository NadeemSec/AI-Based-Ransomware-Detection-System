from datetime import datetime
import os

LOG_FILE = "logs/activity_log.txt"

os.makedirs("logs", exist_ok=True)

def save_log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")