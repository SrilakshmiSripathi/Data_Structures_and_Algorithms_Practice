#LCS-practice

def LCS(a,b):
    la = len(a)+1 # len of a
    lb = len(b)+1 # len of b
    
    m =[[0 for i in range(la)] for j in range(lb)]

    for i in range(1, la):
        
        for j in range(1, lb):
            if a[i-1] == b[j-1]:
                m[i][j] = m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i][j-1], m[i-1][j])
    print( m, m[la-1][lb-1])

    common_string = ""
    i = len(m)
    j = len(m)
    while i>=0:
        while j>=0:
            if a[i-1] == b[j-1]:
                i -= i-1
                j -= j-1
            else:
                
    for i in range(len(m)):
        for j in range(len(m)):
            if :
                common_string += a[i-1]
                direction = m[i-1][j-1]
            else:
                common_string += m[(max(m[i][j-1], m[i-1][j]))]
    return common_string
                

aa = [1,2,3]
bb = [1,2,3]

print(LCS(aa,bb))

#aaa = [1,2,3,4]
#bbb = [1,2,3]

#print(LCS(aaa,bbb))
