class Solution(object):
    def advantageCount(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = sorted(a)
        b = sorted(b)
        i = 0
        while i < len(a):
            if a[i] >= b[i]:
                print a[i],b[i]
                pass
            else:
                
                for val in range(len(a[i+1::])):
                    print val
                    if a[val] > b[i]:
                        a[i], a[val]= a[val], a[i]
            i = i + 1
           
        return a
    

#A = [2,7,11,15]
#B = [1,10,4,11]
A = [12,24,8,32]
B = [13,25,32,11]
n = Solution()
print n.advantageCount(A,B)
