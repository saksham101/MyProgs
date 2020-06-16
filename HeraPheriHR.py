# SOLUTION
import math

pq = input().split()
if int(pq[0]) < int(pq[1]) :
    print(math.factorial(int(pq[0])))
else :
    print(math.factorial(int(pq[1])))
