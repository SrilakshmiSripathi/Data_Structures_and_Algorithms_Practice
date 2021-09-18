num = [1,3,2,4,0,-1,-2]
n = len(num)
for i in range(n):
    for j in range(i,n):
        if num[i] > num[j]:
            num[i],num[j] = num[j], num[i]
print(num)
