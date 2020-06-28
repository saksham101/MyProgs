"""
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Input Format

The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
Explanation

Given the following return dates:
Actual: 
Expected: 

Because , we know it is less than a year late.
Because , we know it's less than a month late.
Because , we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be . We then print the result of  as our output.


"""
# SOLUTION
# Enter your code here. Read input from STDIN. Print output to STDOUT
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1 > y2 :
        fine = 10000
    if y1 == y2 :
        if m1 > m2 :
            fine = (m1-m2)*500
        if m1 == m2 :
            if d1 > d2 :
                fine = (d1-d2)*15
            else:
                fine = 0
    return fine

d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])
d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])
result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)
