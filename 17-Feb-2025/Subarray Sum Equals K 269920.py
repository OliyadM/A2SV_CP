# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution(object):
    def subarraySum(self, nums, k):
        pre_sum = {0: 1}
        run_sum = 0
        count = 0

        for num in nums:
            run_sum += num
            if (run_sum - k) in pre_sum:
                count += pre_sum[run_sum - k]
            if run_sum in pre_sum:
                pre_sum[run_sum] += 1
            else:
                pre_sum[run_sum] = 1
        
        return count
