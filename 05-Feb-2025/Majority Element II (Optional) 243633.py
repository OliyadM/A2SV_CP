# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        k=int(n/3)
        freq_dect = Counter(nums)
        result=[]
        for key , value in freq_dect.items():
            if value > k:
                result.append(key)
        return result