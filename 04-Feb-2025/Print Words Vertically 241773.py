# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution(object):
    def printVertically(self, s):
        s = s.split()
        longest_string = max(s, key=len)  
        n = len(longest_string)  
        lst = [""] * n  
        for word in s:
            for i in range(len(word)):
                lst[i] += word[i]
            for i in range(len(word), n):
                lst[i] += " "
        for i in range(len(lst)):
            lst[i] = lst[i].rstrip()
        return lst
