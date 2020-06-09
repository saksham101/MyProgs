/*
Task

Implement a function named factorial that has one parameter: an integer, . It must return the value of  (i.e.,  factorial).

Input Format

Locked stub code in the editor reads a single integer, , from stdin and passes it to a function named factorial.

Output Format

The function must return the value of .

Sample Input 0

4
Sample Output 0

24
*/
// SOLUTION
/*
 * Create the function factorial here
 */
function factorial(n){
    if( n == 1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
}

function main() {
    const n = +(readLine());
    
    console.log(factorial(n));
}
