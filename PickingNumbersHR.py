"""
Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is , you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.

Function Description

Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.

pickingNumbers has the following parameter(s):

a: an array of integers
Input Format

The first line contains a single integer , the size of the array .
The second line contains  space-separated integers .

Constraints

The answer will be .
Output Format

A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is .

Sample Input 0

6
4 6 5 3 3 1
Sample Output 0

3
Explanation 0

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e.,  and ), so we print the number of chosen integers, , as our answer.

Sample Input 1

6
1 2 2 3 1 2
Sample Output 1

5
Explanation 1

We choose the following multiset of integers from the array: . Each pair in the multiset has an absolute difference  (i.e., , , and ), so we print the number of chosen integers, , as our answ
"""
# SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    # Write your code here
    k = 0
    b = [0]*100
    try :
        for i in range(0,len(a)) :
            for j in range(0,len(a)) :
                k = 2*i
                if a[i] == a[j] or a[i] == a[j]+1 :
                    b[k] += 1
                if a[i] == a[j] or a[i] == a[j]-1 :
                    b[k+1] += 1
    except :
        pass
    Max = b[0];       
    for i in range(0, len(b)):    
        if(b[i] > Max):    
            Max = b[i]
    print(Max)
        
n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)
