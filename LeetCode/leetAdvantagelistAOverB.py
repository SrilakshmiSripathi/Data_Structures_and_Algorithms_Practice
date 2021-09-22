'''
You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

Example 1:

Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
 

Constraints:

1 <= nums1.length <= 105
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 109
'''

class Solution(object):
    def advantageCount(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        
        #a = sorted(a)
        #b = sorted(b)
        i = 0
        while i < len(a):
            if a[i] <= b[i]:                
                for val in range(len(a[i+1::])):
                    print (val)
                    if a[val] > b[i]:
                        a[i], a[val]= a[val], a[i]
            i = i + 1
           
        return a"""
        i = 0
        j = 0
        while j < len(a)-1:
            while a[i] < b[j] and i < len(a)-1:
                a[i], a[i+1] = a[i+1], a[i]
                i +=1
            j +=1
        return a
                
                
                
                

        

    
    

#A = [2,7,11,15]
#B = [1,10,4,11]
A = [12,24,8,32]
B = [13,25,32,11]
n = Solution()
print (n.advantageCount(A,B))
