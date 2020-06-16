# SOLUTION
N = int(input())
s1 = str(input())
s2 = str(input())
while(N>0):
    s1_count , s2_count  = 0 , 0
    string = str(input())
    for i in range(max(len(s1),len(s2))) :
        if s1.startswith(string, i):
            s1_count+=1
        if s2.startswith(string, i):
            s2_count+=1
    if s1_count > 0 and s2_count > 0:
        print("YES")
    else :
        print("NO")
    N -= 1
