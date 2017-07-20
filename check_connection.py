import os
import argparse

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
    response = os.system("speedtest-cli --simple")
    print(response)
