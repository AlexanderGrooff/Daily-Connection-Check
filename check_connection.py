import os

response = os.system("ping -c 1 -w2 8.8.8.8 > /dev/null 2>&1")

if response == 0:
    print("Connection is up")
else:
    print("Connection is down")

