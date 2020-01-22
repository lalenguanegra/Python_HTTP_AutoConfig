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



