int solve(int A, int B, int C, int D) {
    
    int temp = C, count = 0;
    if(C%D != 0){
        temp+=D;
        temp -=((C)%D);
    }
    while(temp <= B-A){
        temp += D;
        count += 1;
    }
    cout<< count;
}
