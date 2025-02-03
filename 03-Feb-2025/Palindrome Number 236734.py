# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        str_int=str(x)
        return str_int ==str_int[::-1]   
        