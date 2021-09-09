def Counting(m):
    n = len(m)
    count = 0
    rows = 0
    i = 0
    while i < n:
        c = 0
        print (i,c,"\t i,c")
        if m[i][c] == 1:
            print("if1 \t m[i][c]",m[i][c])
            c = c + 1
        elif m[i][c] == 0:
            print("\n \t m[i][c]",m[i][c])
            if count < c:
                print ("else")
                count = c
                rows = i
        i = i+1
    return rows
narray = [[1,1,1,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,0,0,0,0,0],
          [1,1,1,1,0,0]]
print (Counting(narray))

