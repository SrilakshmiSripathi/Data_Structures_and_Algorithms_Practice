def find_element(nums, target):
    length = len(nums)
    st = 0
    ed = length-1
    while st < ed:
        mid = (st + ed + 1) // 2
        if nums[mid][1] > target:
            ed = mid - 1
        else:
            st = mid
    return nums[st]

def UptimalUtilization(a, b, target):
    a.sort(key=lambda x:x[1])
    b.sort(key=lambda x:x[1])
    len1 = len(a)
    len2 = len(b)
    curval = 0
    res = []
    for idx1, num1 in a:
        idx2, num2 = find_element(b,target-num1)
        if num1 + num2 <= target:
            print(num1+num2)
            if curval < num1 + num2:
                curval = num1 + num2
                res = [[idx1, idx2]]
            elif curval == num1 + num2:
                res.append([idx1, idx2])
    return res


a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
#print(UptimalUtilization(a, b, target))


print (UptimalUtilization([(1,2000),(2,3000),(3,6000)],
	 [(1,2000)], 7000))
