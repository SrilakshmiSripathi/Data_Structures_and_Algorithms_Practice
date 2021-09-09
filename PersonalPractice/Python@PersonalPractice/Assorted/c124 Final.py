def matrix(AMatrix):
    n = len(AMatrix)
    row = 0
    column = 0
    for i in range(n):
        if AMatrix[i][column] == 1 and column >= 0:
            column += 1
            row = i
    return row

x = [[1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1, 0, 0, 0],]

y = [[1, 1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1, 0],
     [1, 1, 1, 1, 0, 0],
     [1, 1, 1, 1, 0, 0],
          ]
print (matrix(x))
print (matrix(y))
