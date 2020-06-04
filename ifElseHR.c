*/
Task

Given a positive integer denoting n, do the following:

If 1<=n<=9 then print the lowercase English word corresponding to the number (e.g., one for , two for , etc.).
If n>9 print Greater than 9.
Input Format

The first line contains a single integer denoting .

Output Format

If , then print the lowercase English word corresponding to the number (e.g., one for , two for , etc.); otherwise, print Greater than 9 instead.

Sample Input

5
Sample Output

five
Sample Input #01

8
Sample Output #01

eight
Sample Input #02

44
Sample Output #02

Greater than 9

/*
// SOLUTION
#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n ;
    char *string[10] = { "one","two","three","four","five","six","seven","eight","nine"};
    scanf("%d",&n);
    if( n >=1 && n<= 9)
    {
        printf("%s",string[n-1]);
    }
    else
    printf("Greater than 9");

    return 0;
}
