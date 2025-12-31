import os
import sys
from logo import logo
from license_gate import check_license

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("""
==============================
 F VIRUS PEGASUSA TANZANIA
==============================

[1] Generate QR Code (VIEW ONLY)
[0] Exit
""")

def run_qr():
    os.system("python3 web/qr_view.py")

if __name__ == "__main__":
    clear()
    logo()
    check_license()

    while True:
        menu()
        choice = input("Select option: ").strip()

        if choice == "1":
            run_qr()
        elif choice == "0":
            print("Goodbye 👋")
            sys.exit(0)
        else:
            print("Invalid option\n")













