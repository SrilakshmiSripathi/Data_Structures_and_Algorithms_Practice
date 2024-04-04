'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrom.
A palindrom is a word or phrase that is the same forwards and backwards. 
A permutation is a rearrangement of letters. 
The palindrom does not need to be limited to just dictionary words. 
You can ignore casing and non-letter characters. 
Examples
Input: Tact coa
Output: True(permutations: 'taco cat', 'atco cta', etc.)
'''

# Solution 1: Use a dictionary to count the number of each character

def palindromePermutation(s:str) -> bool:
    s = s.lower() # ignore casing
    s = s.replace(' ', '') # ignore non-letter characters
    s = ''.join(sorted(s)) # sort the string
    odd = 0 # count the number of odd characters
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            i += 1
        else:
            odd += 1
    if odd > 1:
        return False
    else:
        return True

# Test
print(palindromePermutation('Tact coa')) # True
print(palindromePermutation('Tact coaa')) # False
print(palindromePermutation('Tact coaA')) # True

# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Follow up
def palindromePermutation(s:str) -> bool:
    s = s.lower() # count the number of odd characters
    odd = 0
    for i in range(26):
        print(ord('a')+i)
        print(chr(ord('a')+i))
        if s.count(chr(ord('a')+i)) % 2 == 1:
            odd += 1
    if odd > 1:
        return False
    else:
        return True

# Test
print(palindromePermutation('Tact coa')) # True
print(palindromePermutation('Tact coaa')) # False

# Time Complexity: O(n)
# Space Complexity: O(1)