def CountOnes(A, n):
    num = 0
    j=0
    for i in range(n-1,0):
        while(A[i][j] != 0):
            j += 1
        num += j
    return num


narray = [[1, 1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1]]
print (CountOnes(narray,len(narray)))
