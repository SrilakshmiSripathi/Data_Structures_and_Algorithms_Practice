'''
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Give two strings, write a function to check if they are
one edit(or zero edits) away.
Example:
pale, ple -> true
pales, pale->true
pale, bale-> true
pale, bake -> false
'''

import unittest


def one_edit_away(input_string1, input_string2):
    "For a given string checking if the string is one edit away"
    cols = len(input_string1) + 1  # 5 0PALE n
    rows = len(input_string2) + 1  # 4 0PLE m
    edits = [[0]*cols]*rows  # 5 cols 4 rows n m
    print(edits)
    for row in range(rows+1): #m
        for col in range(cols+1): #n
            if row == 0:
                edits[row][col] = col
            elif col == 0:
                edits[row][col] = row
            elif input_string1[col-1] == input_string2[row-1]:

                edits[row][col] = edits[row-1][col-1]
                print(edits[row][col],
                      "edits[row-1][col-1]")
            else:
                edits[row][col] = 1 + \
                    min(edits[row-1][col], edits[row]
                        [col-1] + edits[row-1][col-1])
                print(edits[row][col],
                      "print(edits[row][col])")
            print(edits)
    return True if edits[-1][-1] <= 1 else False


print(one_edit_away("pale", "ple"))
print(one_edit_away("pales", "pale"))
print(one_edit_away("pale", "bale"))
print(one_edit_away("pale", "bake"))


class Test(unittest.TestCase):
    "Test"

    def is_one_edit_away_test(self: 'Test') -> None:
        """Checks check_permutation fucntion"""
        self.assertEqual(one_edit_away("pale", "ple"), True, "Should be True")
        self.assertEqual(one_edit_away("pales", "pale"), True,
                         "Should be True")  # this case is not covered by code
        self.assertEqual(one_edit_away("pale", "bale"), True, "Should be True")
        self.assertEqual(one_edit_away("pale", "bake"),
                         False, "Should be False")


if __name__ == "__main__":
    unittest.main()
