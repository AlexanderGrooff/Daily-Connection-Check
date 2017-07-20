import os
import subprocess
import argparse
import re

parser = argparse.ArgumentParser(description="Routine internet quality checker")
parser.add_argument("-t", "--type", action="store", default="ping", help="Set to either ping or speedtest", choices=["ping", "speedtest"])

args = parser.parse_args()

if args.type == "ping":
    response = os.system("ping -c 1 -w2 8.8.8.8 > /dev/null 2>&1")

    if response == 0:
        print("Connection is up")
        #os.system("echo \"Success\" | mail -s \"Ping success\" alexbotmailer@gmail.com")
    else:
        print("Connection is down")
        os.system("echo \"Failure\" | mail -s \"Ping failure\" alexbotmailer@gmail.com")
if args.type == "speedtest":
    response = str(subprocess.check_output("speedtest-cli --simple", shell=True))
    # 'Ping: 6.886 ms\r\nDownload: 10.96 Mbit/s\r\nUpload: 12.04 Mbit/s\r\n'
    # re.S for . to also include newline chars
    groups = re.search(r"Ping: (.*) ms.*Download: (.*) Mbit.*Upload: (.*) Mbit", response, re.S)
    print(response)
    print(groups.group(1), groups.group(2), groups.group(3))
