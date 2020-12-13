#include <bits/stdc++.h>
using namespace std;


int main() {
    int n , temp ,a,b;
    vector<int>v;
    cin>>n;
    for (int i = 0 ; i< n ;i++)
    {
        cin>>temp;
        v.push_back(temp);
    }   
    cin>>temp;
    v.erase(v.begin() +temp-1);
    
    cin>>a>>b;
    v.erase(v.begin()+a-1,v.begin()+b-1);
    
    cout<<v.size()<<endl;
    for(int i = 0 ;i < v.size() ;i ++){
        cout<<v.at(i)<<" ";
    }
    return 0;
}
