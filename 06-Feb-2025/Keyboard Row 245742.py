# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        result=[]
        for word in words:
            w=set(word.lower())
            if w<=r1 or w<=r2 or w<=r3:
                result.append(word)
        return result