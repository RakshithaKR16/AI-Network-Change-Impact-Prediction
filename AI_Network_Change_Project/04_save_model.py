import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("network_change_dataset.csv")

# Encode columns
change_encoder = LabelEncoder()
impact_encoder = LabelEncoder()

df["change_type"] = change_encoder.fit_transform(df["change_type"])
df["impact"] = impact_encoder.fit_transform(df["impact"])

# Features
X = df[
    [
        "latency_ms",
        "packet_loss_percent",
        "bandwidth_mbps",
        "throughput_mbps",
        "device_status",
        "link_status",
        "change_type"
    ]
]

# Target
y = df["impact"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "network_impact_model.pkl")

# Save encoders
joblib.dump(change_encoder, "change_type_encoder.pkl")
joblib.dump(impact_encoder, "impact_encoder.pkl")

print("================================")
print("MODEL SAVED SUCCESSFULLY")
print("================================")

print("network_impact_model.pkl")
print("change_type_encoder.pkl")
print("impact_encoder.pkl")