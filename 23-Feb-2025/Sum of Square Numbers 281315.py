# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/


class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(c**(0.5))
        while left <= right:
            squaresum = left**2 + right**2
            if squaresum == c:
                return True  
            elif squaresum > c:
                right -= 1  
            else:
                left += 1  
        return False