'''URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has suggicient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
(Note: if implementing in Java, please use a character array so that you can
 perform this operation in place.)
Example
Input: 'Mr John Smith ',13
Output: 'Mr%20John%20Smith',13
'''

import unittest


def urlify(input_string, string_length):
    """return string replacing spaces when input is string"""
    i = 0
    new_string = ''
    while i <= string_length-1:
        if input_string[i] == ' ' and i != string_length-1:
            new_string += input_string[i].replace(' ', '%20')
        else:
            new_string += input_string[i]
        i += 1
    return new_string


print(urlify('te st ', 6))
print(urlify('te st', 5))
print(urlify('Mr John Smith ', 13))
print(urlify("test ", 4))


class Test(unittest.TestCase):
    """Tests"""

    def is_urlify_test(self: 'Test') -> None:
        """Checks check_permutation fucntion"""
        self.assertEqual(urlify("te st ", 6), 'te%20st', 'Should be te%20st')
        self.assertEqual(urlify("te st", 5), 'te%20st', 'Should be te%20st')
        self.assertEqual(urlify('Mr John Smith ', 13),
                         'Mr%20John%20Smith', 'Should be Mr%20John%20Smith')
        self.assertEqual(urlify("test ", 4), 'test', 'Should be test')


if __name__ == "__main__":
    unittest.main()
