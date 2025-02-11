# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution(object):
    def targetIndices(self, nums, target):
        a=sorted(nums)
        result=[]
        for i in range(len(a)):
            if a[i] == target:
                result.append(i)
        return result
        