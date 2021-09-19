# Function for finding least possible root of any positive integer number
def iroot(k,n):
    if(k > 0 and n > 0):
        x = 1
        for i in range(0,n):
            # Finding exponent of every number from 0 to n
            x = i ** k
            if(x == n):
                # checking x value and n
                return i
            elif (x > n):
                # check if x value is greater than the n value,
                #if yes least possible cube is 1 less than i
                return i-1
    else:
        return("\t k or n value is non-positive integer")

print (iroot(3,124))
#4
print (iroot(3,125))
#5
print (iroot(3,126))
#5
print (iroot(5,625))
#3
print (iroot(4,128))
#3
