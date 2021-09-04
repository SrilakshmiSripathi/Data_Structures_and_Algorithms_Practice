def palindrome(num):
    a = str(num)
    b = a[::-1]
    if a == b:
        return True

def product():
    i = 999
    while i >= 100:
        j = 999
        while j >= 100:            
            c = i*j
            if palindrome(c) == True:
                return c
        j -= 1
    i -= 1

print product()
