# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        m = len(matrix)       
        n = len(matrix[0])    
        
        arr = []
        for _ in range(n):
            row = m * [0]     
            arr.append(row)
        
        
        for i in range(m):
            for j in range(n):
                arr[j][i] = matrix[i][j]
                
        return arr
