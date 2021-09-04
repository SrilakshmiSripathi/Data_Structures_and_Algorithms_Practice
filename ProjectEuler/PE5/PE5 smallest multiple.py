n = 0
for i in xrange(2,1000000000):
    for j in range(20,0,-1):
        if i%j != 0:
            break
        else:
            n=i
    if j == 0:
        break
            
