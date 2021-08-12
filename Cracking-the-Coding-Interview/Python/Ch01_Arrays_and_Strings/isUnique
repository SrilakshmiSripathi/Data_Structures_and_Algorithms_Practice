"""

Problem statement:
Implement an algorithm to determing if a string has all unique characters.
What if you cannot use additional data structures?

"""

import unittest

def isUnique(inputString):
    # Add each char in string to a dict
    char_dict = {}

    # by default, if the length is 0, the string is unique
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
        self.assertEqual(isUnique("thisis"), False, "Should be False")
    def test_single(self):
        self.assertEqual(isUnique("this"), True, "Should be True")
    def test_sentense(self):
        self.assertEqual(isUnique("abcdefgh"), True, "Should be True")

   
if __name__ == "__main__":
    unittest.main()
