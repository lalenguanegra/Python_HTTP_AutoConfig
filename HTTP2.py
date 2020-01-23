import re
import qrcode
import os
import time
str = open('ip.txt', 'r').read()
http=('http://')
port =(':8000')
all = (http+str+port)
all = re.sub(r"[\n\t\s]*", "", all)
print(all)
img = qrcode.make(all)
img.save('ip.png')
time.sleep(5)
os.system('start ip.png')


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "YOUR_NAME@gmail.com"  
receiver_email = "OTHER_PERSON@gmail.com" 
password ="MY_Password"
message = """\
Subject: Python HTTP Server
URL
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message+all)