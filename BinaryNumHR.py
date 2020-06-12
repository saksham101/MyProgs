"""
Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of  is , so the maximum number of consecutive 's is .

Sample Case 2:
The binary representation of  is , so the maximum number of consecutive 's is .
"""
# SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
print(max(len(length) for length in bin(n)[2:].split('0')))
