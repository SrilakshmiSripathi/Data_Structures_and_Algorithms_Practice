## find connecting bridges without overlap, kind of DP problem

n = len(n1)+1

m = [[0 for i in range(n)] for j in range(n)]

count = [0] * n
for i in range(1, n):
    for j in range(1, n):
        if n1[i-1] == n2[j-1]:
            m[i][j] = m[i-1][j-1] + 1
        else:
            m[i][j] = max(m[i-1][j], m[i][j-1])
print(m[-1][-1])


#n1 = [1,4,2]
#n2 = [1,2,4]

#n1 = [2,5,1,2,5]
#n2 = [5,2,1,5,2]

#n1 = [1,7,1,7,5]
#n2 = [1,9,2,5,1]

n1 = [9,2,5,1,2,5]
n2 = [10,5,2,1,5,2]
