factors = [[1],]

def fac(x):
    temp =[]
    for num in range(1,x+1):
        if x%num == 0:
            temp.append(num)
    return temp

triangleSequence = [1,]
i = 2
while len(factors[-1]) < 501:
    temp = triangleSequence[-1] + i
    triangleSequence.append(temp)
    factors.append(fac(temp))
    print (factors)
    i +=1
    
print ((triangleSequence[-1]))


