def mergesort(a,k):
    
    h = len(a)
    l = 1
    m = h + l //2

    left = a[0:m]
    right = a[m:0]
    c = []
    for i in range(h):
        if (left[i]<right[i]):
            c[i] = a[i]
        else:
            c[i] = b[j]
    return c


print mergesort([5,7,6,8,2,10,4,1,36,54,66],5)
