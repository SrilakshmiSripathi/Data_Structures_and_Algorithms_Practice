def missing(a):
    """ Input: an array with number from 1 to n+1
        Output: missing number"""
    start = 0
    end = len(a)-1
    diff = (a[end] - a[start])/end
    mid = end -(start)/2
    while start <= end:
        # Checking left subarray only
        if mid + 1 < end and a[mid] - a[mid-1] != diff:
            return a[mid-1] - diff
        # Checking right subarray only
        elif mid - 1 >= start and a[mid] - a[mid-1] != diff:
            return a[mid-1] + diff
        # Checking near mid point in right sub tree
        elif a[mid]-a[0] != (mid-0)*diff:
            end = mid-1
        # Checking near mid point in left sub tree
        else:
            start = mid + 1


k = [1,2,3,5,6,7,8,9,10]
print missing(k)
x =[5,7,9,13,15]
print missing(x)
