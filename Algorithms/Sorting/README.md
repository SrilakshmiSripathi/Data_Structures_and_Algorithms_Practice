# 									Stable Sorts

# Bubble Sort

```
num = [1,3,2,4,0,-1,-2]
n = len(num)
for i in range(n):
    for j in range(i,n):
        if num[i] > num[j]:
            num[i],num[j] = num[j], num[i]
print(num)
Output: [-2,-1,0,1,2,3,4]
```

#### Properties and important notes
1. Above is the efficient version of Bubble sort(traditional sort starts the jth index from 0, but starting from i makes it better)
2. Sort still takes ```O(n^2)``` worst case Time Complexity and ```O(n)``` space complexity.
3. This is a stable sort, as it does not change order of the elements. (if they are two elements with in different index, their relative index is maintained).
4. Reccurent relation ```T(n) = 2T(n/2) + θ(n)```
5. Bubble sort uses exchange algorithm paradigm.
6. Not exactly a in-place sorting algorithm.


# Merge Sort

```
def MergeSort(a):
    # base case
    if len(a) == 0 or len(a) == 1:
        return a[:len(a)]
    mid = len(a)//2
    L = MergeSort(a[:mid])
    R = MergeSort(a[mid:])
    newList = merge(L, R)
    return newList

def merge(left, right):
    results = []
    i, j = 0, 0
    #print(left)
    #print(right)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i]) # smaller one into the result
            i = i + 1
        else:
            results.append(right[j])
            j = j + 1
    results = results + left[i:] + right[j:]
    return results
```

#### Properties and important notes

# Insertion Sort

```
def isort(a):
    for i in range(1,len(a)):
        currentvalue = a[i]
        position = i

        while position>0 and a[position-1]> currentvalue:
            a[position] = a[position-1]
            position = position -1
        a[position] = currentvalue
    return a
```

#### Properties and important notes


# Shell Sort

```

```

#### Properties and important notes


# Bucket Sort

```

```

#### Properties and important notes


# Radix Sort

```

```
#### Properties and important notes


# 									Unstable Sorts

# Quick Sort

### Recursive Algorithm
```
def quickSort(ls):
    quickSortRecurr(ls, 0, len(ls)-1)

def quickSortRecurr(ls, first, last):
    if first < last:
        mid = partition(ls, first, last)
        quickSortRecurr(ls, first, mid-1)
        quickSortRecurr(ls, mid+1,last)

def partition(ls, first, last):
    pivot = ls[first]
    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and ls[left] <= pivot:
            left += 1
        while right >= left and ls[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            ls[left],ls[right] = ls[right], ls[left]
        ls[first], ls[right] = ls[right], ls[first]
    return right
```

#### Iterative algorithm

```
def quick_sort_iterative(list_, left, right):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left,right))
    
    #Main loop to pop and push items until stack is empty
    while temp_stack:      
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))

def partition(list_, left, right):
    """
    Partition method
    """
    #Pivot first element in the array
    piv = list_[left]
    i = left + 1
    j = right
 
    while 1:
        while i <= j  and list_[i] <= piv:
            i +=1
        while j >= i and list_[j] >= piv:
            j -=1
        if j <= i:
            break
        #Exchange items
        list_[i], list_[j] = list_[j], list_[i]
    #Exchange pivot to the right position
    list_[left], list_[j] = list_[j], list_[left]
    return j

```

#### Properties and important notes

# Selection Sort

```

```
#### Properties and important notes


# Heap Sort

#### Min Heap without libraries 
```
def heapsort(lst):
    
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)//2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    right = root *2 +2
    if child > end:
        break
    if right <= end and lst[child] < lst[right]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      return
```

#### Max Heap without libraries
```
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
```

#### Properties and important notes