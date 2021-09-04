def primality(num):
    for i in range(2,num-1):
        if num % i == 0:
            return False
    else:
        return True

total = 0
for i in range(2000000,2):
    if primality(i) == True:
        total += i
print (total) 
