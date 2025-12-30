import os
import sys

# FORCE python kuona folder ya main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from logo import logo
from license_gate import check_license
from android.adb_usb import adb_usb
from android.adb_wifi import adb_wifi


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

        # 🔐 LICENSE CHECK (MUST PASS)
        check_license()

        while True:
            menu()
            choice = input("Select option: ").strip()

            if choice == "1":
                adb_usb()

            elif choice == "2":
                adb_wifi()

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


