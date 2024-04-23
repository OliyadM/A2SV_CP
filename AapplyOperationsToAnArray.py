class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        new_nums = []
        count_zeros = 0
        for num in nums:
            if num == 0:
                count_zeros += 1
            else:
                new_nums.append(num)
        new_nums += [0] * count_zeros
        return new_nums
