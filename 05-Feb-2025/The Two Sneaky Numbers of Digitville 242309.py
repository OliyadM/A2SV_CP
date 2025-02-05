# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

from collections import Counter
class Solution(object):
    def getSneakyNumbers(self, nums):
        result=[]
        freq_dect=Counter(nums)
        for key,value in freq_dect.items():
            if value >1:
                result.append(key)
        return result
