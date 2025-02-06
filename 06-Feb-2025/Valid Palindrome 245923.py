# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        newstr=""
        for char in s:
            if char.lower().isalnum():
                newstr+=char.lower()
        return newstr==newstr[::-1]

