import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# -----------------------------------
# 1. Load dataset
# -----------------------------------

df = pd.read_csv("network_change_dataset.csv")

# -----------------------------------
# 2. Encode text columns
# -----------------------------------

change_encoder = LabelEncoder()
impact_encoder = LabelEncoder()

df["change_type"] = change_encoder.fit_transform(df["change_type"])
df["impact"] = impact_encoder.fit_transform(df["impact"])

# -----------------------------------
# 3. Select input features
# -----------------------------------

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

# -----------------------------------
# 4. Split data
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------------
# 5. Create Random Forest model
# -----------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# -----------------------------------
# 6. Train model
# -----------------------------------

model.fit(X_train, y_train)

# -----------------------------------
# 7. Make predictions
# -----------------------------------

y_pred = model.predict(X_test)

# -----------------------------------
# 8. Accuracy
# -----------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("RANDOM FOREST MODEL RESULTS")
print("================================")

print("\nAccuracy:")
print(f"{accuracy * 100:.2f}%")

# -----------------------------------
# 9. Classification report
# -----------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=impact_encoder.classes_
    )
)

# -----------------------------------
# 10. Confusion matrix
# -----------------------------------

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# -----------------------------------
# 11. Feature importance
# -----------------------------------

print("\nFeature Importance:")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)