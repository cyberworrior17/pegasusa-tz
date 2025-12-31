import json
import sys
from datetime import datetime

def check_license():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)

        key = input("Enter License Key: ").strip()

        if key != config["license_key"]:
            print("\n[!] WRONG LICENSE KEY")
            print("Check @uknown_virus404x for another password")
            sys.exit(1)

        expiry = datetime.strptime(config["expiry"], "%Y-%m-%d")
        if datetime.now() > expiry:
            print("\n[!] LICENSE EXPIRED")
            print("Contact admin: @uknown_virus404x")
            sys.exit(1)

        print("\n[✓] LICENSE ACCEPTED\n")

    except Exception as e:
        print("[!] LICENSE SYSTEM ERROR")
        print(e)
        sys.exit(1)




