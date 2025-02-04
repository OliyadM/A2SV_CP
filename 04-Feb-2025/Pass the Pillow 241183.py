# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution(object):
    def passThePillow(self, n, time):
        p = 1
        d = 1
    
        for i in range(time):
            p += d
            if p == n:
                d = -1
            elif p == 1:
                d = 1

        return p
        