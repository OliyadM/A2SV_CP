# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        if k==1:
            return max(nums)
        n=len(nums)
        left=0
        max_sum=cur_sum=sum(nums[:k])
        for right in range(k,n):
            cur_sum=cur_sum+nums[right]-nums[left]
            max_sum=max(cur_sum,max_sum)
            left+=1
        
        return float(max_sum) / float(k)


