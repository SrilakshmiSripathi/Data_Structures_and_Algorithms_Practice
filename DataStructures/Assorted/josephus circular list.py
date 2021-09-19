def josephus(n, k):
    a = list(range(1, n + 1))
    a[n - 1] = 0
    p = 0
    v = []
    while a[p] != p:
        for i in range(k - 2):
            p = a[p]
        v.append(a[p])
        a[p] = a[a[p]]
        p = a[p]
    v.append(p)
    return v
 
print (josephus(10, 4))
# k = 2 [1, 3, 5, 7, 9, 2, 6, 0, 8, 4]
# k = 4 [3, 7, 1, 6, 2, 9, 8, 0, 5, 4]
 
print (josephus(41, 3))
30
