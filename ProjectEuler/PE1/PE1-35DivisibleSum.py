def div(num):
    for i in range(num):
        sums=0
        if i%3==0 or i%5==0:
            sums = sums +i
    return sums

print div(1000)
