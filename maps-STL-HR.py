#include <bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n , val;
    map<string,int>m;
    string name;
        int marks, q;
        cin>>n;
    for(int i=0;i<n;i++)
    {
        
        cin>>q>>name;
        if(q==1){
            cin>>marks;
            m[name] += marks;
        }
        if(q==2){
            m.erase(name);
        }
        if(q==3){
            cout<<m[name]<<endl;
        }
        
    }
    return 0;
}
