# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        twice_s = s + s
        
        if goal in twice_s:
            return True
        else:
            return False
