import subprocess
import platform


def ping_device(ip_address):
    print("\nTesting device:", ip_address)
    print("--------------------------------")

    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", ip_address]
    else:
        command = ["ping", "-c", "4", ip_address]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode == 0:
        print("TEST RESULT: PASS")
        return True
    else:
        print("TEST RESULT: FAIL")
        return False


print("====================================")
print("   AI NETWORK AUTOMATED TEST")
print("====================================")

ip = input("Enter device IP address: ")

ping_device(ip)