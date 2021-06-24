#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby 
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    pairs = 0
    ar.sort()
    if n == len(ar):
        pass
    else:
        return "Number input and length of array doesn't match"
    
    groupbylist = [list(j) for i, j in groupby(ar)]
    
    for group in groupbylist:
        if len(group) % 2 == 0:
            pairs+= len(group)/2
        else:
            pairs+= len(group)//2
    return int(pairs)