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

```

#### Properties and important notes

# Insertion Sort

```

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

```

```
#### Properties and important notes

# Selection Sort

```

```
#### Properties and important notes


# Heap Sort

```

```
#### Properties and important notes