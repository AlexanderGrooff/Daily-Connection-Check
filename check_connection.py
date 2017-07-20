import os

response = os.system("ping -c 1 -w2 8.8.8.8 > /dev/null 2>&1")

if response == 0:
    print("Connection is up")
    #os.system("echo \"Success\" | mail -s \"Ping success\" alexbotmailer@gmail.com")
else:
    print("Connection is down")
    os.system("echo \"Failure\" | mail -s \"Ping failure\" alexbotmailer@gmail.com")
