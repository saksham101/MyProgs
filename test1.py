# with  http://py4e-data.dr-chuck.net/comments_244952.xml used as count.txt
url = input('Enter - ')
xml = open(url)
sum=0
for line in xml :
    if line.startswith("<count>") :
        pos=line.find("<count>")
        pos2=line.find("</count")
        num = line[pos+7 : pos2]
        num = int(num)
        sum+=num
print(sum)
