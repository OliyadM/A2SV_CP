# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i] ==nums[i+1]:
                nums[i]*=2
                nums[i+1] =0
        count=0
        result=[]
        print(nums)
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                count+=1
        print(result)
        for i in range(count):
            result.append(0)
        return result
