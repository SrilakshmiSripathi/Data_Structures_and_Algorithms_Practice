""" Given numbers are in range from 1,n+1
and one number is missing from the same range"""
def missing(a):
    """Input: An sorted array
        Ouput: Missing number is the array"""
    start, end = 0, len(a)-1
    diff = (a[end] - a[start])/end
    mid  = start - (start-end)/2
    value1 = findMissing(a,mid+1,end,diff)
    value2 = findMissing(a,start,mid-1,diff)
    return max(value1,value2)

def findMissing(a, al, ah, dif):
    "recursively search for missing number using difference"
    if al > ah:
        return None
    else:
        print ah,ah-1,"\t",a[ah] - a[ah-1]
        if ah > 1 and a[ah] - a[ah-1] == dif:
            findMissing(a, al, ah-1, dif)
        else:
            return a[ah] + dif

l = [10,15,25,30,35]
print missing(l)

k = [1,2,3,5,6,7,8,9,10]
print missing(k)
