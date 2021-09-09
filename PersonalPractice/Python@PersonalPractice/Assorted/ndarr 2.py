def LoopArray(alist):
    for i in range(len(alist)):
        if alist[i] == 0: 
            return i

def Main(amatrix):
    count = 0
    for alst in amatrix:
        count += LoopArray(alst)
    return count
            
narray = [[1,1,0,0],[1,0,0,0],[1,1,1,0],[1,1,1,0]]

print(Main(narray))
