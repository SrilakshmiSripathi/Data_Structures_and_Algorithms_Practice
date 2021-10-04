def find_max(A):
    m, n = len(A), len(A[0])
    print(A)
    for i in range(m-1):
        for j in range(n-1):
            print(A[i][j], A[i][j + 1] - 1)
            A[i][j] = max(A[i][j], A[i][j + 1] - 1)
            print(A)
        for j in range(n):
            A[i][j] = max(A[i][j], A[i][j - 1] - 1 if j else 0)
            A[i + 1][j] += A[i][j]
        print(A)
    return max(A[-1])

x = [[1,0,0,0,1],
     [1,0,0,0,0]]
p = [[1,2,3],
     [1,5,1],
     [3,1,1]]
q = [[1,5],
     [2,3],
     [4,2]]
print(find_max(q))
            
                



            
                    
                    
    
