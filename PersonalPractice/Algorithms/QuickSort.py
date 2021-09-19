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

alist = [39,2,3,1,4,5,68,9]
quickSort(alist)
print(alist)
