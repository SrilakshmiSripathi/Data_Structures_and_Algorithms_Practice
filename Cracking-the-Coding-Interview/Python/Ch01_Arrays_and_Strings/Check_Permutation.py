'''
Check Permutation: Given two strings,
write a method to decide if one is a permutation of the other.
Eg: 
ex1 = (s1='test', s2='stet', True)
ex2 = (s1='ab', s2='eidbaooo', True)
ex3 = (s1='ab', s2='eidboaoo', False)
Constraints: 1 <= s1.length, s2.length <= 104 
s1 and s2 consist of lowercase English letters.
'''

# Brute force

import unittest

def checkPermutation(s1, s2):
    n = len(s1)
    i = 0
    flag = False
    while i <= n+2:
        if s1[i] == s2[i]:
            flag = True
            i += 1
        else:
            # to get the length of permutation return i value
            return flag, i

def isPermutation(s1, s2):
    # s1='test', s2='stet'
    # s1='ab', s2='eidbaooo'
    s1 = sorted(s1) #estt,ab,ab
    s2 = sorted(s2) #estt,abdeiooo,eidboaoo

    l1 = len(s1)
    l2 = len(s2)

    if l1 <= l2:
        flag, length = checkPermutation(s1, s2)
    elif l2 < l1:
        flag, length = checkPermutation(s2, s1)
    return (flag, length)

class Test(unittest.TestCase):
    def isPermutation(self):
        self.assertEqual(isPermutation("test", "stet"), (True,4), "Should be True")
        self.assertEqual(isPermutation("ab", "eidbaooo"), (True,2), "Should be True")
        #self.assertEqual(isPermutation("ab", "eidboaoo"), (False,0) "Should be False")
        

if __name__ == "__main__":
    unittest.main()






