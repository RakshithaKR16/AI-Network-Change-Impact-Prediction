
import pandas as pd
import joblib

# Load trained model and encoders
model = joblib.load("network_impact_model.pkl")
change_encoder = joblib.load("change_type_encoder.pkl")
impact_encoder = joblib.load("impact_encoder.pkl")

print("=" * 45)
print(" AI + CISCO ADAPTIVE NETWORK VALIDATION")
print("=" * 45)

print("\nAvailable network changes:")
for change in change_encoder.classes_:
    print("-", change)

print("\nEnter network parameters")

latency = float(input("Latency (ms): "))
packet_loss = float(input("Packet loss (%): "))
bandwidth = float(input("Bandwidth (Mbps): "))
throughput = float(input("Throughput (Mbps): "))
device_status = int(input("Device status (1=Working, 0=Failed): "))
link_status = int(input("Link status (1=Working, 0=Failed): "))
change_type = input("Change type: ").strip()

# Validate inputs
if change_type not in change_encoder.classes_:
    print("ERROR: Invalid change type.")
    raise SystemExit

if not (0 <= packet_loss <= 100):
    raise ValueError("Packet loss must be between 0 and 100.")

if min(latency, bandwidth, throughput) < 0:
    raise ValueError("Latency, bandwidth and throughput cannot be negative.")

if device_status not in (0, 1) or link_status not in (0, 1):
    raise ValueError("Device and link status must be 0 or 1.")

# Prepare ML input
change_encoded = change_encoder.transform([change_type])[0]

input_data = pd.DataFrame([{
    "latency_ms": latency,
    "packet_loss_percent": packet_loss,
    "bandwidth_mbps": bandwidth,
    "throughput_mbps": throughput,
    "device_status": device_status,
    "link_status": link_status,
    "change_type": change_encoded
}])

# AI prediction
prediction = model.predict(input_data)[0]
impact = impact_encoder.inverse_transform([prediction])[0]
probabilities = model.predict_proba(input_data)[0]
confidence = max(probabilities) * 100

print("\n--- AI PREDICTION ---")
print("Change:", change_type)
print("Predicted impact:", str(impact).upper())
print(f"Confidence: {confidence:.2f}%")

# Adaptive validation test selection
print("\n--- ADAPTIVE VALIDATION ---")

tests = []

# Common checks for every scenario
tests.append((
    "Device status",
    device_status == 1
))
tests.append((
    "Link status",
    link_status == 1
))

# Select extra tests based on change type
if change_type == "normal":
    tests.append(("Packet loss within demo limit", packet_loss <= 1))
    tests.append(("Latency within demo limit", latency <= 100))

elif change_type == "high_latency":
    tests.append(("High latency detected", latency > 100))
    tests.append(("Packet loss within demo limit", packet_loss <= 1))

elif change_type == "packet_loss":
    tests.append(("Packet loss detected", packet_loss > 1))

elif change_type == "router_failure":
    tests.append((
        "Failure indicators detected",
        device_status == 0 or link_status == 0
        or packet_loss >= 100
    ))

# Display selected checks
for test_name, passed in tests:
    print(f"{test_name}: {'PASS' if passed else 'FAIL'}")

# Overall network health
healthy = (
    device_status == 1
    and link_status == 1
    and packet_loss <= 1
    and latency <= 100
)

print("\n--- FINAL RESULTS ---")
print("Network health:", "HEALTHY" if healthy else "PROBLEM DETECTED")
print("Health test:", "PASS" if healthy else "FAIL")

# Did the tests confirm the selected scenario?
if change_type == "normal":
    scenario_confirmed = healthy
elif change_type == "high_latency":
    scenario_confirmed = latency > 100
elif change_type == "packet_loss":
    scenario_confirmed = packet_loss > 1
else:
    scenario_confirmed = (
        device_status == 0 or link_status == 0
        or packet_loss >= 100
    )

print(
    "Scenario validation:",
    "CONFIRMED" if scenario_confirmed else "NOT CONFIRMED"
)
print("=" * 45)

import csv
from datetime import datetime

print("\n--- CISCO TEST RESULT LOG ---")

cisco_result = input(
    "Enter actual Cisco ping result (PASS/FAIL): "
).strip().upper()

if cisco_result not in ["PASS", "FAIL"]:
    print("Invalid result. Enter PASS or FAIL.")
else:
    with open("cisco_test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            change_type,
            str(impact),
            round(confidence, 2),
            cisco_result
        ])

    print("Cisco result saved successfully!")
    print("AI prediction:", str(impact).upper())
    print("Actual Cisco ping:", cisco_result)