def isort(a):
    for i in range(1,len(a)):
        currentvalue = a[i]
        position = i

        while position>0 and a[position-1]> currentvalue:
            a[position] = a[position-1]
            position = position -1
        a[position] = currentvalue
    return a
#return a,a[0],a[len(a)-1] 

lista =[55,2,100,54,1000,1,687,6,1011]
print (isort(lista))
