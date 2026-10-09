
import platform
import subprocess
import re
import csv
from datetime import datetime

# Use a reachable endpoint for testing
target = input("Enter reachable IP or hostname: ").strip()

if not target:
    raise SystemExit("Please enter a valid target.")

count = "4"

if platform.system().lower() == "windows":
    command = ["ping", "-n", count, "-w", "2000", target]
else:
    command = ["ping", "-c", count, "-W", "2", target]

print(f"\nRunning automatic ping test for {target}...\n")

result = subprocess.run(
    command,
    capture_output=True,
    text=True,
    timeout=15
)

output = result.stdout + result.stderr
print(output)

# Extract packet statistics
sent = received = lost = None
latency = None

match = re.search(
    r"Sent\s*=\s*(\d+),\s*Received\s*=\s*(\d+),\s*Lost\s*=\s*(\d+)",
    output,
    re.IGNORECASE
)

if match:
    sent, received, lost = map(int, match.groups())
    loss_percent = lost / sent * 100 if sent else 100
else:
    loss_percent = None

# Extract average latency on Windows
match = re.search(
    r"Average\s*=\s*(\d+)\s*ms",
    output,
    re.IGNORECASE
)

if match:
    latency = int(match.group(1))

status = (
    "PASS" if received is not None and received > 0
    else "FAIL"
)

print("========== TEST SUMMARY ==========")
print("Target:", target)
print("Packets sent:", sent if sent is not None else "Unknown")
print("Packets received:", received if received is not None else "Unknown")
print(
    "Packet loss:",
    f"{loss_percent:.1f}%" if loss_percent is not None else "Unavailable"
)
print("Average latency:", f"{latency} ms" if latency is not None else "Unavailable")
print("Connectivity:", status)

with open("auto_network_results.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        datetime.now().isoformat(timespec="seconds"),
        target, sent, received,
        loss_percent, latency, status
    ])

print("\nResults saved to auto_network_results.csv")
