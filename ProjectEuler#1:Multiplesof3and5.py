"""
If we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Find the sum of all the multiples of  or  below .

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

For each test case, print an integer that denotes the sum of all the multiples of  or  below .

Sample Input 0

2
10
100
Sample Output 0

23
2318
Explanation 0

For , if we list all the natural numbers below  that are multiples of  or , we get  and . The sum of these multiples is .

Similarly for , we get .

"""
# SOLUTION
#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    num_of_multiples_of_3 = (n-1)//3
    num_of_multiples_of_5 = (n-1)//5
    num_of_multiples_of_15 = (n-1)//15
    sum = (3 * num_of_multiples_of_3 * ( num_of_multiples_of_3 + 1 ) // 2
    + 5 * num_of_multiples_of_5 * ( num_of_multiples_of_5 + 1 ) // 2 
    - 15 * num_of_multiples_of_15 * ( num_of_multiples_of_15 + 1 ) // 2 )
    print(int(sum))
