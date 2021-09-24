def MinMax(a):
    if a[0] < a[1]:
        mini = a[0]
        maxi = a[1]
    else:
        mini = a[1]
        maxi = a[0]
    
    i = 3
    while i < len(a)+1:
        try: 
            j = i - 1
            print (i,j, len(a))
            if a[i] > a[j]:
                if a[i] > maxi:
                    maxi = a[i]
                if a[j] < mini:
                    mini = a[j]
            else:
                if a[i] < mini:
                    mini = a[i]
                if a[j] > maxi:
                    maxi = a[j]
        except IndexError:
            if a[j] < mini:
                mini = a[j]
            elif a[j] > maxi:
                maxi = a[j]
        i = i + 2
    return mini, maxi
                

b = [7, 1, 3, 5, 9, 12, 54, 71, 33, 2, 11, 62, 90]
k = [9, 2, 55, 65, 73, -1, 49, 51, 200, 857, 3, 763, -5, 656, 33, -2]
print (MinMax(b))
print (MinMax(k))
