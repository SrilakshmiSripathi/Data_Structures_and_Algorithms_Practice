def BubbleSort(num):
    n = len(num)
    for i in range(n):
        for j in range(i,n):
            if num[i] > num[j]:
                num[i],num[j] = num[j], num[i]
    print(num)

num = [1, 3 ,2 ,4 ,0 ,-1 ,-2]
nums2 = [0.5, 0.2, -0.1, 0.0]
BubbleSort(num)
BubbleSort(nums2)