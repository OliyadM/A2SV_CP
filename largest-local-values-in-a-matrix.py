class Solution(object):
    def largestLocal(self,grid):
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                max_val = 0
                for k in range(3):
                    for l in range(3):
                        max_val = max(max_val, grid[i + k][j + l])
                maxLocal[i][j] = max_val

        return maxLocal
