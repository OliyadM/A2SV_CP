# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s_dect = Counter(s)
        t_dect = Counter(t)
        for key ,value in s_dect.items():
            if t_dect[key]!=value:
                return False
        return True 