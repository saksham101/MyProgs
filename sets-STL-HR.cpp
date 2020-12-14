#include <bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n, q, val;
    set<int> s;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>q>>val;
        if(q == 1){
            s.insert(val);
        }
        else if(q == 2){
                s.erase(val);
            }
        else{
            cout<<(s.find(val) == s.end() ? "No" : "Yes")<<endl;
        }
    }
    return 0;
}
