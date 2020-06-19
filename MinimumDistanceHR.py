"""
We define the distance between two array values as the number of indices between the two values. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, print .

For example, if , there are two matching pairs of values: . The indices of the 's are  and , so their distance is . The indices of the 's are  and , so their distance is .

Function Description

Complete the minimumDistances function in the editor below. It should return the minimum distance between any two matching elements.

minimumDistances has the following parameter(s):

a: an array of integers
Input Format

The first line contains an integer , the size of array .
The second line contains  space-separated integers .

Constraints

Output Format

Print a single integer denoting the minimum  in . If no such value exists, print .

Sample Input

6
7 1 3 4 1 7
Sample Output

3
Explanation
Here, we have two options:

 and  are both , so .
 and  are both , so .
The answer is .
"""
# SOLUTION
def minimumDistances(a):
    d = []
    for i in a:
        if (len(a)-1 - a[::-1].index(i)) - a.index(i) != 0 :
            d.append((len(a)-1 - a[::-1].index(i)) - a.index(i)) 
    if len(d) == 0:
        print("-1")
    else :
        print(min(d))

n = int(input())
a = list(map(int, input().rstrip().split()))
minimumDistances(a)

