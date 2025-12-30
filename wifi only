import os

def adb_wifi():
    print("[*] Make sure phone & PC are on same Wi-Fi")
    ip = input("Enter phone IP:PORT (e.g 192.168.1.5:5555): ")
    os.system(f"adb connect {ip}")
    os.system("scrcpy")

