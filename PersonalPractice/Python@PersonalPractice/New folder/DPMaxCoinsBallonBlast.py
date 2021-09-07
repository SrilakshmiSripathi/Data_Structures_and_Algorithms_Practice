class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        nums = [1] + nums + [1]

        f = [[0] * (N + 2) for _ in range(N + 2)]

        for length in range(2, N + 2):
            for i in range(N - length + 2):
                j = i + length
                mij = nums[i] * nums[j]
                for mid in range(i + 1, j):
                    v = f[i][mid] + f[mid][j] + mij * nums[mid]
                    if v > f[i][j]:
                        f[i][j] = v

        return f[0][N + 1]

def maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1]+[n for n in nums if n!=0]+[1]
    regional_max_coins = [[0 for i in xrange(len(nums))] for j in xrange(len(nums))]
    for balloons_to_burst in xrange(1, len(nums)-1): # number of balloons in (l,r) region
        for l in xrange(0, len(nums)-balloons_to_burst-1): # for m and r to be assigned legally
            r = l+balloons_to_burst+1
            for m in xrange(l+1,r):
                regional_max_coins[l][r] = max(regional_max_coins[l][r], regional_max_coins[l][m]+regional_max_coins[m][r]+nums[l]*nums[m]*nums[r])
    return regional_max_coins[0][-1]
