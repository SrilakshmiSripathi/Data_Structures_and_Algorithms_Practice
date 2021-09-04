"""
num,k = 1,1
prime = []
while k < 20:
   for i in range(1,num):
      if num%i !=0:
         print i,num
   p = [i for i in range(1,num) if num%i !=0]
   if p not in prime:
      prime += p
   num +=1
   k  += 1
print prime,len(prime)-1,
"""

def primality(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    else:
        return True

k = 0
primes = [1,]
num = 2
while k < 10005:
   if primality(num) == True:
      primes.append(num)
      k += 1
   num +=1
print primes[10001],len(primes),primes[0],primes[1]   
