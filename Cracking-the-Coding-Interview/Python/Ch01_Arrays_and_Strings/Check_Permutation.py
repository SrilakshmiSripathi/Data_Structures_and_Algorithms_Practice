"""check_permutation Given two strings,
write a method to decide if one is a permutation of the other.
Eg:
ex1 = (s1='test', s2='stet', True)
ex2 = (s1='ab', s2='eidbaooo', True)
ex3 = (s1='ab', s2='eidboaoo', False)
Constraints: 1 <= s1.length, s2.length <= 104 s1 and s2 consist of lowercase English letters.
"""

# Brute force

import unittest

def check_permutation(s_1, s_2):
    """computes if the string is a permutation"""
    n_length = len(s_1)
    i = 0
    flag = False
    while i <= n_length+2:
        if s_1[i] == s_2[i]:
            flag = True
            i += 1
        else:
            # to get the length of permutation return i value
            return flag, i

def is_permutation(s_1, s_2):
    """receives inputs"""
    # s1='test', s2='stet'
    # s1='ab', s2='eidbaooo'
    s_1 = sorted(s_1) #estt,ab,ab
    s_2 = sorted(s_2) #estt,abdeiooo,eidboaoo

    l_1 = len(s_1)
    l_2 = len(s_2)

    if l_1 <= l_2:
        flag, length = check_permutation(s_1, s_2)
    elif l_2 < l_1:
        flag, length = check_permutation(s_2, s_1)
    return (flag, length)

class Test(unittest.TestCase):
    """Tests"""
    def is_permutation_test(self: 'Test') -> None:
        """Checks check_permutation fucntion"""
        self.assertEqual(is_permutation("test", "stet"), (True,4), "Should be True")
        self.assertEqual(is_permutation("ab", "eidbaooo"), (True,2), "Should be True")
        self.assertEqual(is_permutation("ab", "eidboaoo"), (False,0), "Should be False")

if __name__ == "__main__":
    unittest.main()
