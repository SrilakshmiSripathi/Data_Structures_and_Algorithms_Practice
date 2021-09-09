##
##def mm(m):
##    c,t = 0,0
##    row = 0
##    for r in range(len(m)):
##        print (m[r],r,c)
##        if m[r][c] == 1 and c >= 0:
##            c = c+1
##            row = r
##    return row
##
##
##narray = [[1,1,1,0,0,0],
##          [1,0,0,0,0,0],
##          [1,0,0,0,0,0],
##          [1,0,0,0,0,0],
##          [1,0,0,0,0,0],
##          [1,0,0,0,0,0]]
##print (mm(narray))

def mm(m):
    r = 0
    t =0
    row = 0
    for c in range(len(m)):
        print (r,c,t,row,"\t r,c,t,row")
        if m[r][c] == 0:
            if c > t:
                t = c
                row = r
        else:
            r = r+1
    return (row)

narray = [[1,1,1,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,1,1,1,1,0],
          [1,0,0,0,0,0]]
print (mm(narray))
