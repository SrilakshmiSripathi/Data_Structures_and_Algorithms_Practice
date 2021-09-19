def IsMaxHeap(a,i,n):
        """
        Input: individual array elements
        Ouput: sorting elements to form heap
        RT: log n
        """
        heapSize = n - 1 # heapsize <= list size
        parent = 2*i//2
        left = 2*i
        right= 2*i + 1

        largest = 0
        for i in range(0,n):
            # Check left child and parent
            if ((left <= heapSize) and a[left] > a[i]):
                largest = left
            else:
                largest = i
            # Check right child and align
            if((right <= heapSize) and a[right] > a[i]):
                largest = right
            if(largest != i):
                a[i],a[largest]=a[largest],a[i]
        return a

def Building(a,n):
    """
    Input: Unsorted array of len n
    Output: Array bottom up manner converts to heap
    Running time n, (as n = len of array)
    """
    for i in range(n,1,-1):
        IsMaxHeap(a,i,n)

def HeapSort(a):
    """
    Input: Unsorted array of len n
    Output: sorted array from smallest to largest
    RT: nlog n, (n is len(a))
    """
    n = len(a)
    Building(a,n)
    for i in range(n-1,0,1):
        a[i],a[0]=a[0],a[i]
        IsMaxHeap(a,i,0)
    return(a)



k = [1,2,3,4,5,6,7,8,9,9010,11,12,13,14,15,46,50,80]

print(HeapSort(k))
