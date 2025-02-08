# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution(object):
    def findRotation(self, mat, target):
            for _ in range(4):
                mat=[list(row)[::-1] for row in zip(*mat)]
                if mat == target:
                    return True
            return False
        