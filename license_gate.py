import json
import sys
from datetime import datetime

def check_license():
    try:
        # Soma config.json
        with open("config.json", "r") as f:
            config = json.load(f)

        print("\n==============================")
        print("   F-VIRUS LICENSE SYSTEM")
        print("==============================")

        # Uliza license key
        user_key = input("Enter License Key: ").strip()

        # Kagua key
        if user_key != config["license_key"]:
            print("\n[!] WRONG LICENSE KEY")
            print("You can check @uknown_virus404x for another password")
            sys.exit(1)

        # Kagua expiry
        expiry_date = datetime.strptime(config["expiry"], "%Y-%m-%d")
        if datetime.now() > expiry_date:
            print("\n[!] LICENSE EXPIRED")
            print("Contact admin: @uknown_virus404x")
            sys.exit(1)

        # Ikitokea ni sahihi
        print("\n[✓] LICENSE ACCEPTED")
        print("Welcome to F-Virus Tool")
        print("Owner:", config.get("owner", "Mr.Virus"))
        print("==============================\n")

    except FileNotFoundError:
        print("\n[!] ERROR: config.json haipo")
        sys.exit(1)

    except Exception as e:
        print("\n[!] LICENSE SYSTEM ERROR")
        print(e)
        sys.exit(1)

