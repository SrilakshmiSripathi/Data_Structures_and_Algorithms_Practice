'''triangleSequence = [1,]

i = 2
while i < 13:
    triangleSequence.append(triangleSequence[-1] + i)
    i +=1
print (triangleSequence)
'''
factors = []
n = 5000
while len(factors[-1]) < 501:
    nxt = n *(n+1)/2
    
