# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution(object):
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
            left += 1
            right -= 1

        return True
