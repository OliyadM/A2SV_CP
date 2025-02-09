# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution(object):
    def findDiagonalOrder(self, mat):
       
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        i, j = 0, 0  

        while len(result) < m * n:  
            while i >= 0 and j < n:
                result.append(mat[i][j])
                i -= 1  
                j += 1  

            if j == n:  
                i += 2  
                j -= 1  
            else:
                i += 1  

            while j >= 0 and i < m:
                result.append(mat[i][j])
                i += 1  
                j -= 1  

            if i == m:  
                j += 2  
                i -= 1  
            else:
                j += 1  

        return result
