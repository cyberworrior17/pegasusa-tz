import json
from datetime import datetime
import sys

def check_license():
    try:
        with open("config.json","r") as f:
            data = json.load(f)

        key = input("Enter License Key: ").strip()
        if key != data["license_key"]:
            print("Invalid license!")
            print("You can check @uknown_virus404x for another password")
            sys.exit()

        expiry = datetime.strptime(data["expiry"], "%Y-%m-%d")
        if datetime.now() > expiry:
            print("License expired!")
            sys.exit()

        print("License OK ✔")

    except Exception as e:
        print("License error:", e)
        sys.exit()
