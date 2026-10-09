import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("network_change_dataset.csv")

# Convert text columns into numbers
change_encoder = LabelEncoder()
impact_encoder = LabelEncoder()

df["change_type"] = change_encoder.fit_transform(df["change_type"])
df["impact"] = impact_encoder.fit_transform(df["impact"])

# Input features
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

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("DATA PREPROCESSING COMPLETED")
print("--------------------------------")

print("Total samples:", len(df))
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nTraining feature shape:", X_train.shape)
print("Testing feature shape:", X_test.shape)

print("\nEncoded change types:")
print(dict(zip(
    change_encoder.classes_,
    change_encoder.transform(change_encoder.classes_)
)))

print("\nEncoded impact levels:")
print(dict(zip(
    impact_encoder.classes_,
    impact_encoder.transform(impact_encoder.classes_)
)))

print("\nSample training data:")
print(X_train.head())

print("\nSample target values:")
print(y_train.head())