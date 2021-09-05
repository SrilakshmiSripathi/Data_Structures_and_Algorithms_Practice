#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    s1 = set(s1)
    print(s1)
    for i in s2:
        print(i)
        if i in s1:
            return "YES"
    return "NO"
    
def twoStrings2(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input().strip())
    q = ['hello','world','hi','world']
    q2 = ['wouldyoulikefries','cabcabcabcabcabc','hackerrankcommunity',\
          'cdecdecdecde','jackandjill', 'wentupthehill','writetoyourparents','fghmqzldbc']
    q3= ['aardvark','apple','beetroot','sandals']

    #for q_itr in range(0,len(q)-1,2):
    #for q_itr in range(0,len(q2)-1,2):
    for q_itr in range(0,len(q3)-1,2):
        #s1 = q[q_itr]
        #s2 = q[q_itr+1]

        #s1 = q2[q_itr]
        #s2 = q2[q_itr+1]

        s1 = q3[q_itr]
        s2 = q3[q_itr+1]

        result = twoStrings(s1, s2)

        #result2 = twoStrings2(s1, s2) 

        print(result + '\n')
        #print(result2 + '\n')


