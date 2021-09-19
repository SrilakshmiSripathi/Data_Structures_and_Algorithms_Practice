def x(some_list):
    for i in range(len(some_list)):
        if some_list[i] == 0:
            print (i)
            return int(i)


def Counting(ndarray):
    count = 0
    rows = 0
    value =0
    for i in ndarray:
        value = x(i)
        if count < value:
            count = value
            rows = i
    return (rows,"row has,",count,"this many 1's")

narray = [[1,1,0],[1,0,0],[1,1,1]]
print (Counting(narray))


##
##
##
##i,j = 0,0
##count = 0
##row = 0
##while i < n and j < n:
##    print (i,j)
##    if ndarray[i][j] != 0:
##        j += 1
##    else:
##        if count < j-1:
##            count = j-1
##            row = i
##            print (count,row)
##            j += 1
##    i += 1
##    

    
