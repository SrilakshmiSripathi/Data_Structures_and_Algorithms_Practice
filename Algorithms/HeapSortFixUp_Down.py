import time

def newheap(n):
    return [0]*(n+1)

def heapfixup(a,i):
    while i>1:
        p = i//2
        if a[p] > a[i]:
            a[i], a[p] = a[p],a[i]
            i = p
        else:
            return

def heapfixdown(a,i):
    p = 2*i
    l = 2*i+1
    while p <= a[i]:
        
        if l <= a[i]:
            if a[l] < a[p]:
                p += 1
        if a[i] > a[p]:
            a[i],a[p] = a[p],a[i]
            i = p
            print a
        else:
            return

def HeapSort(a,k):
    n = len(a)
    b = newheap(n)
    for i in range(n):
        if b[1] < a[i]:
            b[1] = a[i]
            heapfixdown(b,1)
        else:
            heapfixup(b,i)
            return b

print HeapSort([50,2,41,22,30,1,100,80,12],3)
