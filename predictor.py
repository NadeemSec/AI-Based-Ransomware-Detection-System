import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/ransomware_model.pkl")

# Load encoders
encoders = joblib.load("model/encoders.pkl")


def safe_encode(column, value):

    try:
        encoder = encoders[column]

        if value in encoder.classes_:
            return encoder.transform([value])[0]

        return 0

    except:
        return 0


def predict_ransomware(data):

    sample = pd.DataFrame([[
        int(data["Time"]),
        safe_encode("Protocol", "TCP"),
        safe_encode("Flag", "A"),
        safe_encode("Family", "WannaCry"),
        int(data["Clusters"]),
        safe_encode("SeedAddress", "1DA11mPS"),
        safe_encode("ExpAddress", "1BonuSr7"),
        int(data["BTC"]),
        int(data["USD"]),
        int(data["Netflow_Bytes"]),
        safe_encode("IPaddress", "A"),
        safe_encode("Threats", "Bonet"),
        int(data["Port"])
    ]])

    prediction = model.predict(sample)

    return int(prediction[0])