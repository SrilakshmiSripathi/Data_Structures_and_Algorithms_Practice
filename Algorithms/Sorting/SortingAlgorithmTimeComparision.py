import heapq as Hq
import random
from datetime import timedelta
import time


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return alist


def heapSort(alist):
    sort = []
    heapsort = []
    for i in alist:
        Hq.heappush(sort, i)
    Hq.heapify(sort)
    for i in range(len(sort)):
        heapsort.append(Hq.heappop(sort))
    return heapsort


def quickSort(alist):
    quickSort2(alist, 0, len(alist)-1)
    return alist


def quickSort2(alist, first, last):
    if first < last:
        mid = partition(alist, first, last)
        quickSort2(alist, first, mid - 1)
        quickSort2(alist, mid + 1, last)


def partition(alist, start, end):
    pivot = alist[start]
    leftmark = start + 1
    rightmark = end

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1
        while rightmark >= leftmark and alist[rightmark] >= pivot:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] =\
                             alist[rightmark], alist[leftmark]
        alist[start], alist[rightmark] = alist[rightmark], alist[start]
    return rightmark


def printMergeS(alist):
    # Print and calculate runtime for MergeSort
    StartTime = time.time()
    print (mergeSort(alist))
    EndTime = time.time()
    RunTime = EndTime - StartTime
    print ("\n MergeSort Duration:", RunTime)


def printHeapS(alist):
    # Print and calculate runtime for HeapSort
    StartTime = time.time()
    print (heapSort(alist))
    EndTime = time.time()
    RunTime = EndTime - StartTime
    print ("\n HeapSort Duration:", RunTime)


def printQuickS(alist):
    # Print and calculate runtime for QuickSort
    StartTime = time.time()
    print (quickSort(alist))
    EndTime = time.time()
    RunTime = EndTime - StartTime
    print ("\n QuickSort Duration:", RunTime)


def driver():
    x = [1000, 10000, 100000]
    for i in x:
        for k in range(5):
            unsorted = []
            for j in range(i):
                unsorted.append(random.randint(-500, 50000))
            printMergeS(unsorted)
            printHeapS(unsorted)
            printQuickS(unsorted)
driver()
