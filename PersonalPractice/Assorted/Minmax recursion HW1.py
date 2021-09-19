def minmax(a,n,cmin=None,cmax=None):
    if n == 0:
        return cmin,cmax
    if n > 0:
        if a[n-1] > cmax:
            cmax = a[n-1]
        elif a[n-1] < cmin:
            cmin = a[n-1]
        return mm(a,n-1,cmin,cmax)

x=[1]
print mm(x,len(x))
