def fun(strParam):
    count = 0
    outParam = ''
    for i in range(1, len(strParam)):
        if strParam[i] == strParam[i-1]:
            count+=1
        else:
            outParam = outParam + str(count+1) + strParam[i-1]
            count = 0
    outParam = outParam + str(count+1) + strParam[i]
    return outParam
print(fun(input()))
