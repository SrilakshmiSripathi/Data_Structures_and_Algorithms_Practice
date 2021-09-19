##def FindPx(CoefficientArray,n,Xvalue):
##    """Inputs: A coeffients array of a polynomial, x value,
##    length of coefficient array
##    Output: Value of polynomial equation for a x value"""

def Horner(a,n,x):
    sums = a[0]
    for i in range(1,n):
        sums = sums * x + a[i]
    return sums


a = [-1, 2, -6, 2]
x = 3
n = len(a)

print (Horner(a,n,x))
