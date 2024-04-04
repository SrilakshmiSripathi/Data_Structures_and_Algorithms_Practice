"""
Problem statement:
Implement an algorithm to determing if a string has all unique characters.
What if you cannot use additional data structures?
Note: Algorithm assumes strings as input
"""

import unittest

def isUniqueDS(inputString):
    # Add each char in string to a dict
    char_dict = {}

    # when the length is 0 or 1 the string defnitely will be unique
    if len(inputString) == 0 or len(inputString) == 1:
        return True
    
    for i in inputString:
        if i in char_dict:
            return False
        else:
            char_dict[i] = 1
    return True

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(isUniqueDS("thisis"), False, "Should be False")
    def test_single(self):
        self.assertEqual(isUniqueDS("this"), True, "Should be True")
    def test_sentense(self):
        self.assertEqual(isUniqueDS("abcdefgh"), True, "Should be True")

if __name__ == "__main__":
    unittest.main()
