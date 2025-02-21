# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        arr = [0] * (len(nums) + 1)
        for left, right in requests:
            arr[left] += 1
            arr[right + 1] -= 1

        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
        arr.pop()

        arr.sort(reverse=True)
        nums.sort(reverse=True)

        result = 0
        for i in range(len(nums)):
            result += nums[i] * arr[i]
        
        return result % MOD
