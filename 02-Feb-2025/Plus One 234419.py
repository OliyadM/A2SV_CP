# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        str_digits=''
        for digit in digits:
            str_digits+=str(digit)
        int_digits=int(str_digits)+1
        result=[]
        for num in str(int_digits):
            result.append(int(num))
        return result