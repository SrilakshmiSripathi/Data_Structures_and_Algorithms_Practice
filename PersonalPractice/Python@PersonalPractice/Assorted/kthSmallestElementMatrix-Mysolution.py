class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if matrix != []:
            smallest = []
            for i in matrix:
                for j in i:
                    smallest += [j]
            return smallest[k-1]
        else:
            print "empty matrix"

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8,
n = Solution()
print n.advantageCount(matrix,k)
