"""
Given an integer, your task is to find another integer such that their bitwise XOR is maximum.

More specifically, given the binary representation of an integer  of length , your task is to find another binary number  of length  with at most  set bits such that their bitwise XOR is maximum.

For example, let's say that  = "0100" and  = 1. The maximum possible XOR can be obtained with  = "1000", where  XOR  = "1100".

Input Format

The first line of input contains an integer, , the number of tests.

The first line of each test contains a binary string representing .

The second line of each test contains an integer, , denoting the maximum number of set bits in .

Constraints

Output Format

Print exactly  lines. In the  of them, print the string denoting  in the  test case.

Sample Input 0

2
10010
5
01010
1
Sample Output 0

01101
10000
Explanation 0

For the first case, (x xor y) gives 11111 which is the maximum possible number that can be obtained.

In the second case, (x xor y) gives 11010. Note that any other y would given a lesser xor sum.
"""
#SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxXorValue' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING x
#  2. INTEGER k
#

def maxXorValue(x, k):
    # Write your code here
    x = list(str(x))
    value = []
    for i in x :
        if i == '0' and k >0:
            value.append('1')
            k -= 1
        else :
            value.append('0')
    value = ''.join(value)
    return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        y = maxXorValue(s, k)

        fptr.write(y + '\n')

    fptr.close()
