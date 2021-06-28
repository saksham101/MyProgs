#include<bits/stdc++.h>
using namespace std;
int getPairsCount(int arr[], int n, int num)
{
	int count = 0;
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			if ((arr[i] + arr[j]) % num == 0)
				count++;
	return count;
}
int main() {
	int T;
	cin>>T;
	while(T>0){
    int size;
    cin>>size;
    int arr[size];
    for(int i=0; i<size; i++){
        cin>>arr[i];
    }
	int num = 4;
	cout<<getPairsCount(arr, size, num);
	    if(T!=1){
	       cout<<"\n";
	    }
	    T--;
	}
	return 0;
}
