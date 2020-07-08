"""
The prime factors of  are  and .

What is the largest prime factor of a given number ?

Input Format

First line contains , the number of test cases. This is followed by  lines each containing an integer .

Constraints

Output Format

For each test case, display the largest prime factor of .

Sample Input 0

2
10
17
Sample Output 0

5
17
Explanation 0

Prime factors of  are , largest is .
Prime factor of  is  itself, hence largest is .
"""
# SOLUTION
#!/bin/python3

import sys
import math

def maxPrimeFactor(n):
    maxPrime = -1
    while n%2 == 0 :
        maxPrime = 2
        n /= 2

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0 :
            maxPrime = i
            n /= i

    if n > 2 :
        maxPrime = n
    return int(maxPrime)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(maxPrimeFactor(n))
