# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution(object):
    def interpret(self,command):
        result = ''
        n=len(command)
        i=0
        while i<n:
            if command[i] == 'G':
                result+='G'
                i=i+1
            elif command[i] == '(':
                if command[i+1]==')':
                    result+='o'
                    i=i+2
                else:
                    result+='al'
                    i=i+4
        return result