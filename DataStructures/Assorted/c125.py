def matrix(AMatrix):
    n = len(AMatrix)
    row = 0
    column = 0
    print (n,row,column,"n,row,column")
    for i in range(n):
        print('for loop i,n',i,n)
        if AMatrix[i][column] == 1 and column >= 0:
            print (AMatrix[i][column],i, column,"AMatrix[i][column],i, column")
            column += 1
            print("column+1",column)
            row = i
            print ("row,i",row,i)
    return row

x = [[1, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1, 1, 1, 0],]
print (matrix(x))
