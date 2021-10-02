#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    SetsOfLetters = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            currentString = str(sorted(s[j:j+i]))
            if currentString not in SetsOfLetters:
                SetsOfLetters[currentString] = 1
            else:
                count += SetsOfLetters[currentString]
                SetsOfLetters[currentString] += 1
    return count


            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input().strip())
    i1 = [2, 'abba','abcd']
    i2 = [2, 'ifailuhkqq', 'kkkk']
    i3 = [1,'cdcd']
    for q_itr in range(1,len(i1)):
        result = sherlockAndAnagrams(i1[q_itr])
        print(str(result) + '\n')
    for q_itr in range(1,len(i2)):
        result2 = sherlockAndAnagrams(i2)
    for q_itr in range(1,len(i1)):
        result3 = sherlockAndAnagrams(i3)

    result2 = sherlockAndAnagrams(i2)
    result3 = sherlockAndAnagrams(i3)
    
    print(str(result2) + '\n')
    print(str(result3) + '\n')


