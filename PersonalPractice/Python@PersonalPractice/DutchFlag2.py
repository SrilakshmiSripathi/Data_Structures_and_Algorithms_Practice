nums = [0,2,1,1,0,2,0,1,2]

i,j,k=0,0,len(nums)-1
while j <= k:
    if nums[j] == 0:
        nums[i],nums[j] = nums[j],nums[i]
        i +=1
        j+=1
    elif nums[j] == 1:
        j+=1
    else:
        nums[j],nums[k] = nums[k], nums[j]
        k -= 1
print(nums)
        
