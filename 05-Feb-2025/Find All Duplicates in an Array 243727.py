# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        array=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                array.append(nums[i])
        return array