def LargePF(num):
    i = 2
    while i*i < num:
        if num % i == 0:
            num = num/i
        i +=1
    return(num)
print LargePF(600851475143)

    
