# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        maximum=run_sum=nums[0]
        for num in nums[1:]:
            run_sum=max(run_sum+num,num)
            maximum=max(run_sum,maximum)
        return maximum
        


        
