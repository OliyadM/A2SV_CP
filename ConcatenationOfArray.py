class Solution(object):
    def getConcatenation(self, nums):
        newNums=list(nums)
        for num in newNums:
            nums.append(num)
        return nums
