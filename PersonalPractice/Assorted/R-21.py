##def inplace(a):
##    n = len(a)
##    m = n//2
##    print(a)
##    print(m,n)
##        
##    for i in range(m):
##            a[i],a[n-1-i] = a[n-1-i],a[i]
##    return a
##
##array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
##print(inplace(array))


def Reverse(a):
    n = len(a)
    new = [0]*n
    for i in range(0,n):
        new[i] = a[i]
    print new
    for j in range(n-1):
        a[j] = new[n-1-j]
    return a

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(Reverse(array))

