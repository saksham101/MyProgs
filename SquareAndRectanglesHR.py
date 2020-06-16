# SOLUTION
from fractions import gcd
import functools

T = int(input())
while(T>0):
    LB = []
    lb = input().split()
    LB.append(int(lb[0]))
    LB.append(int(lb[1]))
    GCD = functools.reduce(gcd,LB)
    LB[0] , LB[1] = LB[0]/GCD , LB[1]/GCD
    print(int(LB[0] * LB[1]))
    T -= 1
