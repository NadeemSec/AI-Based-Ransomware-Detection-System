import os
import time

folder = "monitored_folder"

os.makedirs(folder, exist_ok=True)

for i in range(20):

    filename = f"{folder}/test_{i}.encrypted"

    with open(filename, "w") as file:
        file.write("fake ransomware activity")

    print(f"Created: {filename}")

    time.sleep(0.3)