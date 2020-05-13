counts=dict()
fhand = open("mbox-short.txt")
names=list()
for line in fhand:
    if line.startswith("From "):
        words=line.split()
        name=words[1]
        names.append(name)
for name in names:
    counts[name]=counts.get(name,0)+1
maxcount=None
maxname=None
for k,v in counts.items():
    if maxcount is None or maxcount < v:
        maxcount=v
        maxcount=k
print(maxname,maxcount)
