def pali(num):
    x = str(num)
    y = x[::-1]
    if x == y:
        return True
    return False

def pprod():
    maxp = 0
    for i in xrange(999,100,-1):
        for j in xrange(999,100,-1):
            p = i*j
            if maxp < p and pali(p):
                print i,j
                maxp = p
    return maxp

print pprod()
