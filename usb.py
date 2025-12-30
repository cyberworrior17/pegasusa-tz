import os

def adb_usb():
    print("[*] Connect phone via USB & allow USB debugging")
    os.system("adb devices")
    input("Press ENTER to start screen mirroring...")
    os.system("scrcpy")

