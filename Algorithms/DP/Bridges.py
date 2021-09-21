import math

#n1 = [1,4,2]
#n2 = [1,2,4]

#n1 = [2,5,1,2,5]
#n2 = [5,2,1,5,2]

#n1 = [1,7,1,7,5]
#n2 = [1,9,2,5,1]

n1 = [9,2,5,1,2,5]
n2 = [10,5,2,1,5,2]

k = 0

count = [0] * len(n1)
for i in range(len(n1)):
    for j in range(i, len(n2)):
        if n1[i] == n2[j] and count[i] == 0 and count[j] == 0:
            k +=1
            
            print(i,j, "\t", n1[i], n2[j])
            count[j] += 1
            print(count)
            #count[j] = 0
        elif count[i] == 1:
            break
        

print(sum(count))
print(k)
            
