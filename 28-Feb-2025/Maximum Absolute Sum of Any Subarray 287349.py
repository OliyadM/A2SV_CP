# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix = 0  
        max_prefix = 0  
        current_prefix = 0  
        
        for num in nums:
            current_prefix += num  
            min_prefix = min(min_prefix, current_prefix)  
            max_prefix = max(max_prefix, current_prefix)  
        
        return abs(max_prefix - min_prefix)  

