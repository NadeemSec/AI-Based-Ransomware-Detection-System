import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("dataset/final(2).csv")

# FIX COLUMNS (safe)
df.columns = [
    "Time","Protocol","Flag","Family","Clusters",
    "SeedAddress","ExpAddress","BTC","USD",
    "Netflow_Bytes","IPaddress","Threats","Port","Prediction"
]

df.dropna(inplace=True)

# =========================
# ENCODING (SAVE ENCODERS)
# =========================
encoders = {}

cat_cols = [
    "Protocol","Flag","Family","SeedAddress",
    "ExpAddress","IPaddress","Threats","Prediction"
]

for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# =========================
# SPLIT
# =========================
X = df.drop("Prediction", axis=1)
y = df["Prediction"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# MODEL
# =========================
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# =========================
# SAVE EVERYTHING
# =========================
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/ransomware_model.pkl")
joblib.dump(encoders, "model/encoders.pkl")

print("MODEL TRAINED & SAVED")