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

inp = [int(i) for i in input("Enter the number to be sorted: ").split(",")]
print("Result:", MergeSort(inp))
