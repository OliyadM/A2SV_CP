# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    n=len(a)
    swaps=0 
    for i in range(n):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
    print("Array is sorted in",swaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
        