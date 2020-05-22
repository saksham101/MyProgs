from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
matter= urlopen(url, context=ctx).read()
sum=0
for line in matter :
    if line.startswith("count") :
        pos = line.find("count")
        num=line[pos+7 :]
        num=int(num)
        sum+=num
print(sum)
