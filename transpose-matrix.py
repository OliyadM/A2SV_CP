class Solution(object):
    def transpose(self,matrix):
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]

        return transposed
