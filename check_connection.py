import os
import subprocess
import argparse
import re
import schedule
import time

parser = argparse.ArgumentParser(description="Routine internet quality checker")
parser.add_argument("-p", "--ping", action="store", nargs="?", type=int, default="5", help="Set timer for ping (in minutes)")
parser.add_argument("-s", "--speedtest", action="store", nargs="?", type=int, default="6", help="Set timer for ping (in hours)")
args = parser.parse_args()
mail_address = "alexbotmailer@gmail.com"

def ping():
    response = os.system("ping -c 1 -w2 8.8.8.8 > /dev/null 2>&1")

    if response == 0:
        print("Connection is up")
        #os.system("echo \"Success\" | mail -s \"Ping success\" alexbotmailer@gmail.com")
    else:
        print("Connection is down")
        os.system("echo \"Failure\" | mail -s \"Ping failure\" {}".format(mail_address))

def speedtest():
    response = str(subprocess.check_output("speedtest-cli --simple", shell=True))
    # 'Ping: 6.886 ms\r\nDownload: 10.96 Mbit/s\r\nUpload: 12.04 Mbit/s\r\n'
    # re.S for . to also include newline chars
    groups = re.search(r"Ping: (.*) ms.*Download: (.*) Mbit.*Upload: (.*) Mbit", response, re.S)
    print(response)
    print(groups.group(1), groups.group(2), groups.group(3))
    os.system("echo {} | mail -s \"Speed report\" {}".format(response, mail_address))

schedule.every(args.ping).minutes.do(ping)
schedule.every(args.speedtest).hours.do(speedtest)

while True:
    schedule.run_pending() # Run schedule
    time.sleep(60) # Wait a minute
