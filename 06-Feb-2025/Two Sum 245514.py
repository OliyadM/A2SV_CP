# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution(object):
    def twoSum(self, nums, target):
        indexed_numbers = []
        for index in range(len(nums)):
            indexed_numbers.append((nums[index], index))
        indexed_numbers.sort()
        
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = indexed_numbers[left][0] + indexed_numbers[right][0]

            if current_sum == target:
                return [indexed_numbers[left][1], indexed_numbers[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []
