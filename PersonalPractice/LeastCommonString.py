## LCS
def LCS(sa, sb):    
    matrix = [[0 for i in range(len(sb)+1)]\
              for j in range(len(sa)+1)]
    
    for i in range(1, len(sa)+1):
        for j in range(1, len(sb)+1):
            if sa[i-1] == sb[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            elif sa[i-1] != sb[j-1]:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    print matrix

    finalstring = []
    i, j = len(matrix)-1, len(matrix[0])-1
    while i > 0 and j > 0:
        if sa[i-1] == sb[j-1]:
            i = i-1
            j = j-1
            finalstring.append(sa[i])
        else:
            if matrix[i-1][j] == matrix[i][j]:
                i = i-1
                j = j
            elif matrix[i][j-1] == matrix[i][j]:
                i = i
                j = j-1
    return "Common Seqence", " ".join(map(str, finalstring[::-1]))
                
a = "TGACCACTGTC"
b = "ACTGACACTGATC"
print LCS(a, b)
