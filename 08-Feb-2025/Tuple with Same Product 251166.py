# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

import math
from collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        product_dect = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_dect[product] += 1
        
        result = 0
        for value in product_dect.values():
            if value > 1:
        
                result += (math.factorial(value) // math.factorial(value - 2)) * 4
        
        return result
