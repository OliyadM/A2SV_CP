# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution(object):
    def separateDigits(self, nums):
        str_list=[]
        for i in nums:
            for j in str(i):
                str_list.append(j)
        return list(map(int,str_list))
