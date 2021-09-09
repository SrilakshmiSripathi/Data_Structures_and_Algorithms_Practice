def FindPx(CoefficientArray,n,Xvalue):
    """Inputs: A coefficients array of a polynomial, x value,
    length of coefficient array
    Output: Value of polynomial equation for a x value"""
    sums = CoefficientArray[0]
    for i in range(1,n):
        px = Xvalue
        for j in range(1,i):
            px = px * Xvalue
        sums = sums + px * CoefficientArray[i]
    return sums

a = [10, -20, 12, -6, 16]
x = 25
n = len(a)

print (FindPx(a,n,x))

