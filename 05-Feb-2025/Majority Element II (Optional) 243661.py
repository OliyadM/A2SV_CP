# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        count_dect=Counter(nums)
        n=len(nums)
        k=int(n/3)
        res=[]
        for key,value in count_dect.items():
            if value >k:
                res.append(key)
        return res