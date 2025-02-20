# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        k=goal
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