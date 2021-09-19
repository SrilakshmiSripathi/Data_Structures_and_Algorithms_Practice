def LoopArray(alist):
    n = len(alist)
    print (n)
    for i in range(n):
        if alist[i] == 0:
            print (i)
            
print (LoopArray([1,1,1,1,1,0]))
