import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load("network_impact_model.pkl")
change_encoder = joblib.load("change_type_encoder.pkl")
impact_encoder = joblib.load("impact_encoder.pkl")

print("========================================")
print(" AI NETWORK CHANGE IMPACT PREDICTOR")
print("========================================")

# Get user input
latency = float(input("Enter latency (ms): "))
packet_loss = float(input("Enter packet loss (%): "))
bandwidth = float(input("Enter bandwidth (Mbps): "))
throughput = float(input("Enter throughput (Mbps): "))

device_status = int(
    input("Device status (1=Working, 0=Failed): ")
)

link_status = int(
    input("Link status (1=Working, 0=Failed): ")
)

print("\nAvailable network changes:")

for change in change_encoder.classes_:
    print("-", change)

change_type = input("\nEnter change type: ")

# Encode change type
change_encoded = change_encoder.transform([change_type])[0]

# Create input data
input_data = pd.DataFrame([{
    "latency_ms": latency,
    "packet_loss_percent": packet_loss,
    "bandwidth_mbps": bandwidth,
    "throughput_mbps": throughput,
    "device_status": device_status,
    "link_status": link_status,
    "change_type": change_encoded
}])

# Prediction
prediction = model.predict(input_data)[0]

# Convert prediction back to text
impact = impact_encoder.inverse_transform([prediction])[0]

# Probability
probabilities = model.predict_proba(input_data)[0]
confidence = max(probabilities) * 100

print("\n========================================")
print("          PREDICTION RESULT")
print("========================================")

print("Network Change :", change_type)
print("Predicted Impact:", impact.upper())
print(f"Confidence      : {confidence:.2f}%")

print("========================================")