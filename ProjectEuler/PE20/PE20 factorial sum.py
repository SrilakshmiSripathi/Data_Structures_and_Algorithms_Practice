s = 1
for i in range(100,1,-1):
   s *= i
print s
sums = 0
x = len((str(s)))
s = str(s)
for j in range(x):
   sums += int(s[j])
print sums

#better:
# reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
