# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution(object):
    def largestNumber(self, nums):
        def com(a,b):
            Suma=str(a)+str(b)
            Sumb=str(b)+str(a)
            return Suma>Sumb
        if sorted(nums)[-1]==0:
            return "0"
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if com(nums[i],nums[j]):
                    nums[i],nums[j]=nums[j],nums[i]
        string=""
        for num in nums:
            string+=str(num)
        return string