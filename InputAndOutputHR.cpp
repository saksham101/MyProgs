/*
Read  numbers from stdin and print their sum to stdout.

Note: If you plan on completing this challenge in C instead of C++, you'll need to use format specifiers with printf and scanf.

Input Format

A single line containing  space-separated integers: , , and .

Constraints

Output Format

Print the sum of the three numbers on a single line.

Sample Input

1 2 7
Sample Output

10
Explanation

The sum of the three numbers is .
*/
// SOLUTION
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int a,b,c;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    cin>>a>>b>>c;
    cout<<a+b+c;  
    return 0;
}
