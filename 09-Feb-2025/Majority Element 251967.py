# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        k=len(nums)/2
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num]+=1
            if freq_dict[num]>k:
                return num
    
    
        