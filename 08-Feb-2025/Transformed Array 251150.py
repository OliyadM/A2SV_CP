# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution(object):
    def constructTransformedArray(self, nums):
        r = [0] * len(nums)
        for i in range(len(nums)):
            j = (i + nums[i]) % len(nums)
            r[i] = nums[j]
        return r