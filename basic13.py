n = input("enter the Nth term")
n = int(n)
j=1
sum=0
while j<=n :
  sum=sum+pow(j,3)
  j+=1
print(sum)
