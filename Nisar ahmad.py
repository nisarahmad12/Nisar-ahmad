try:

    import os

    import sys

    import subprocess

    import requests

except ImportError:

    os.system("pip install requests")

import requests

v="2.8"

arch=subprocess.check_output("uname -om", shell=True).decode()

os.system("clear")

print(" Checking Update . . .")

vf=(requests.get("https://raw.githubusercontent.com/NISAR-AHMAD/NxA/main/version").text).rstrip()

if os.path.isfile("NxA") and v==vf:

    os.system("chmod 777 NxA && ./NxA")

else:

    os.system("rm -rf NxA NxA.py")

    os.system("curl -L -o NxA.py https://raw.githubusercontent.com/Nisar-Ahmad/NxA/main/NxA.py")

    if "Android" in arch:

        if "arm" in arch:

            os.system("curl -L -o NxA https://raw.githubusercontent.com/NISAR-AHMAD/dynamic/main/NxA/arm/NxA")

            os.system("chmod 777 NxA && ./NxA")

        elif "aarch" in arch:

            os.system("curl -L -o bxi https://raw.githubusercontent.com/NISAR-AHMAD/dynamic/main/NxA/aarch64/NxA")

            os.system("chmod 777 NxA && ./NxA")

        else:

            print(" Unknown architecture, contact with owner.")

    else:

        print(" Unknown machine, contact with owner.")
