# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution(object):
    def threeSumClosest(self,nums, target):
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < abs(target - res):
                    res = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s

        return res