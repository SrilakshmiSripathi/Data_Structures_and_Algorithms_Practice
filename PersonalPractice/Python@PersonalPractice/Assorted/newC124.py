##"""
##
##In a matrix 1's are filled first and next filled with 0's
##
##find largest number of ones and in which row?
##
##"""
##
##def FindRow(m):
##    n = len(m)
##    vc, vr = 0, n-1
##    tracker = 0
##    while vr != 0:
##        if m[vr][vc] == 0:
##            if tracker < vr:
##                tracker = vr
##        elif m[vr][vc] == 1:
##            vc += 1
##        else:
##            vr = vr - 1
##    return tracker
##
##           
##narray = [[1,1,0,0],[1,0,0,0],[1,1,1,0],[1,1,1,0]]
##
##print (FindRow(narray))


def F(matrix):
    n = len(matrix)
    rows, total= 0, 0
    while rows < n:
        columns = 0
        while columns < n:
            print (rows, columns)
            if matrix[rows][columns] == 0 and columns > total:
                total = columns
            else:
                columns += 1
        rows += 1
    return total-1

narray = [[1,1,1,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0]]
print (F(narray))

        

