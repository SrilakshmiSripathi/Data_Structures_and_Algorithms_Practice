def newheap(n):
    #returns an empty array of size n+1
    return [0] * (n + 1)


def insert(a, e):
    #inserts the value e into the end of the heap (at position of value of a[0]) and
    # uses heapfixup to maintain the min-heap property
    a[0] = a[0] + 1
    a[a[0]] = e
    heapfixup(a, a[0])

def heapfixup(a, i):
    #maintains the min-heap property (children must be larger than their parents)
    #by checking the child at position i against the parent (p) at position i//2
    #to see if the child is smaller, else it will swap the two and check the next parent
    while i > 1:
        p = i//2
        if a[p] > a[i]:
            a[i], a[p] = a[p], a[i]
            i = p
        else:
            return

def extractsmallest(a):
    #extracts and returns the smallest element and shifts the next smallest up
    e, a[1], a[0] = a[1], a[a[0]], a[0] - 1
    heapfixdown(a, 1)
    return e

def heapfixdown(a, i):
    #maintains the min-heap property by shifting the child (c) at position 2*i
    #or 2*i +1, whichever is smaller, to the root next position up in the min-heap
    #until every child is in a "comfortable" position
    while 2 * i <= a[0]:
        c = 2 * i
        if c + 1 <= a[0]:
            if a[c + 1] < a[c]:
                c = c + 1
        if a[i] > a[c]:
            a[i], a[c] = a[c], a[i]
            i = c
        else:
            return

def heapSort(x):
    #main file
    n = len(x)
    a = newheap(n)
    for i in range(n):
        print x[i]
        insert(a, x[i])
        print a
    print "Done"
    for i in range(n):
        print x[i]
        x[i] = extractsmallest(a)
        print x
    print "Sort done"
    return x

l = [10,5,4,9,3,8,1,7,6,2]
print heapSort(l)
##k = [2,5,16,4,10,23,39,18,26,15] 
##print heapSort(k)
##j = [1,2,5,3,4,6,7]
##print heapSort(j)


