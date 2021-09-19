def solution(S,k):
    new_s = ""
    for i in S:
        if i is not "-":
            new_s += i.upper() 
    print (new_s)
    l = len(new_s)-1
    
    f = ""    
    count = 0
    while count < k and l >= 0:
        f += new_s[l]
        count += 1
        l -= 1
        if count == k and l > -1:
            count = 0
            f += "-"
    return (f[::-1])

given_string = "5F3Z-2e-9-w"
length_set = 4

print (solution(given_string, length_set))
    
