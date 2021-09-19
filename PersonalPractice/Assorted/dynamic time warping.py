## Dynamic time wraping
##1. take 2 string
##2. build distance matrix
##3. parse to see what are string min distances
##done

def BuildMatrix(str1, str2):
    matrix = [[float('inf') for i in range(len(str2))]\
              for j in range(len(str1))]
    return matrix

def DistM(str1, str2):
    m = BuildMatrix(str1, str2)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                print "yes i = j, m loc=",i,j, m[i][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    m[i][j] = m[i-1][j-1]
                elif i - 1 <= 0:
                    m[i][j] = m[i - 1][j] + 0
                elif i == 0 or j == 0:
                    m[i][j] = 0
            elif str1[i] != str2[j]:
                print "\n\t","no i != j, m loc=",i,j, m[i][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    m[i][j] = min(m[i-1][j-1],m[i-1][j],m[i][j-1]) + 1
                elif j - 1 <= 0:
                    m[i][j] = m[i][j-1] + 1
                elif i == 0 or j == 0:
                    m[i][j] = 1
    return m
    
##
##a = "ACTGACACTGATC"
##b = "TGACCACTGTC"
a = "CTGACACTGATC"
b = "GACCACATG"
print len(a), len(b)
print DistM(a,b)
