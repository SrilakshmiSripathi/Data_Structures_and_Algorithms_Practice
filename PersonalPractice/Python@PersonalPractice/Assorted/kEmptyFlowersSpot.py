def kEmptySlots(flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = flowers
        ans = float('inf')
        left, right = 0, k+1
        while right < len(days):
            for i in xrange(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left, right = i, i+k+1
                    break
            else:
                ans = min(ans, max(days[left], days[right]))
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1


flo = [1,3,2]
k = 1
print kEmptySlots(flo, k)

ff = [1,2,4,3]
k = 1
print kEmptySlots(ff, k)

'''
def kEmptySlots(f, k):
    days = [0] * (len(f))
    for i in range(len(f)):
        print f[i]-1, 'days[f[i]-1]', days[f[i]-1]
        days[f[i]-1] = i
    print f, 'f \n days', days
    left = 0
    right = k + 1
    res = float('inf')

    for i in range(right, len(days)):
        if days[i] < days[left] or days[i] <= days[right]:
            if i == right:
                res = min(res,max(days[left], days[right]))
                left = i
                right = k + 1 + i
    return -1 if res == float('inf') else res
flowers = [1,3,2]
k = 1
print kEmptySlots(flowers, k) 
ff = [1,2,3,4]
k = 1
print kEmptySlots(ff, k)


 days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day
        left = 0
        right = k + 1
        res = float('inf')

        while right < len(days):
            for i in range(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    left = i
                    right = k + 1 + i
                else:
                    res = min(res,max(days[left], days[right]))
                    left = right
                    right = right + k + 1
        return res if res < float('inf') else -1


import bisect
def kEmptySlots(flowers, k):
        active = []
        for day, flower in enumerate(flowers, 1):
            i = bisect.bisect(active, flower)
            for neighbor in active[i-(i>0):i+1]:
                if abs(neighbor - flower) - 1 == k:
                    return day
            active.insert(i, flower)
        return -1

flowers = [1,3,2]
k = 1
print kEmptySlots(flowers, k) 
ff = [1,2,3,4]
k = 1
print kEmptySlots(ff, k)'''








