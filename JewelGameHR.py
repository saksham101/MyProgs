"""
You're playing a game in which you're given a sequence of various jewels. If adjacent jewels are of the same type, you can gain 1 point by collecting them (thus removing them from the sequence).

Given a string of lowercase English letters, where each letters represents a different type of jewel, find the maximum score you can obtain by playing the game optimally.

For example, if  = "abccbda", you can play as follows:

Collect "cc". These jewels are removed, the string becomes "abbda", and your score becomes 1.
Collect "bb". The string becomes "ada", and your score becomes 2.
After this, it is impossible to collect any more jewels. Therefore, the answer is 2.

Input Format

The first line contains an integer, , denoting the number of test cases.

Each test contains a single string, .

Constraints

 length of 
Output Format

Print  lines. Each line should contain a single integer denoting the maximum score for the corresponding test case.

Sample Input 0

2
abcddcbd
abcd
Sample Output 0

3
0
Explanation 0

In the first case, we first collect "dd". The jewels now become "abccbd". Then collect "cc" followed by "bb". The jewels now become "ad", and no more jewels can be collected. The final score is , which is the maximum score possible.

In the second case, it is not possible to collect any jewels.
"""
# SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMaxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING jewels as parameter.
#
def getMaxScore(jewels):
    st = []
    i = 0
    count = 0
    while i < len(jewels):
        if len(st)!=0 and st[-1]==jewels[i]:
            i+=1
            st.pop(-1)
            count += 1
        else:
            st.append(jewels[i])
            i+=1
    return count

if _name_ == '_main_':
    t = int(input().strip())
    for t_itr in range(t):
        jewels = input()
        print(getMaxScore(jewels))
