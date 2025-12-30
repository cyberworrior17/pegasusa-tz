import os
import sys
import importlib.util

# ================= PATH FIX =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ANDROID_DIR = os.path.join(BASE_DIR, "android")
WEB_DIR = os.path.join(BASE_DIR, "web")

sys.path.append(BASE_DIR)
sys.path.append(ANDROID_DIR)

from logo import logo
from license_gate import check_license

# ============ LOAD adb_usb.py ============
adb_usb_path = os.path.join(ANDROID_DIR, "adb_usb.py")
spec_usb = importlib.util.spec_from_file_location("adb_usb", adb_usb_path)
adb_usb = importlib.util.module_from_spec(spec_usb)
spec_usb.loader.exec_module(adb_usb)

# ============ LOAD adb_wifi.py ============
adb_wifi_path = os.path.join(ANDROID_DIR, "adb_wifi.py")
spec_wifi = importlib.util.spec_from_file_location("adb_wifi", adb_wifi_path)
adb_wifi = importlib.util.module_from_spec(spec_wifi)
spec_wifi.loader.exec_module(adb_wifi)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    print("""
==============================
 F VIRUS PEGASUSA TANZANIA
==============================

[1] Connect via ADB (USB)
[2] Connect via ADB (Wi-Fi)
[3] QR Code Screen View (VIEW ONLY)
[0] Exit
""")


def run_qr():
    try:
        os.system("python3 web/qr_view.py")
    except Exception as e:
        print("[!] Failed to start QR server")
        print(e)


if __name__ == "__main__":
    try:
        clear()
        logo()

        # 🔐 LICENSE CHECK
        check_license()

        while True:
            menu()
            choice = input("Select option: ").strip()

            if choice == "1":
                adb_usb.adb_usb()

            elif choice == "2":
                adb_wifi.adb_wifi()

            elif choice == "3":
                run_qr()

            elif choice == "0":
                print("\nGoodbye 👋")
                sys.exit(0)

            else:
                print("\n[!] Invalid option, try again\n")

    except KeyboardInterrupt:
        print("\n\n[!] Tool stopped by user")
        sys.exit(0)






