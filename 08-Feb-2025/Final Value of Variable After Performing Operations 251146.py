# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution(object):
    def finalValueAfterOperations(self, operations):
        x=0
        for operation in operations:
            if operation[0] == '-' or operation[-1]=='-':
                x-=1            
            elif operation[0]=='+' or operation[-1]=='+':
                x+=1
        return x