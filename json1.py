from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data= urlopen(url, context=ctx).read()
info = json.loads(data)
sum=0
for item in info['comments']:
    sum+= int(item['count'])
print(sum)
