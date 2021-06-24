import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    if 1 not in c:
        return len(c) // 2
    else:
        
        indices = [i for i, x in enumerate(c) if x == 1]
        
        zero_list = []
        completed_list = []
        for i, v in enumerate(indices):
            if i == 0:
                zero_list.append(v)
                completed_list.append(v)
                continue
            else:
                zero_list.append(v - completed_list[-1] -1)
                completed_list.append(v)
            
        jumps += len(c[indices[-1]+1:]) //2
        for index in zero_list:
            jumps += index//2 + 1
        return jumps