class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        if s == [] or t == []:
            return "invalid"
        if len(s) < len(t):
            return "invalid"
        new = {}
        for _, pos in enumerate(t):
            if pos in s:
                print s, pos, _
                if pos not in new:
                    new[pos] = [_]
                else:
                    new[pos].append(_)
                # new.update({_:[pos]})
        ndarray= []
        for keys in new.values():
            ndarray.append(keys)
         
        return ndarray


S = "ADOBECODEBANC"
T = "ABC"
#Output: "BANC"

n = Solution()

print n.minWindow(S,T)
