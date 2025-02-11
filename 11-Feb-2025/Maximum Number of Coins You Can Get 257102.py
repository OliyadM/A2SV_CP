# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        n=len(piles)
        k=int(n/3)
        i=n-2
        res=0
        for _ in range(k):
            res+=piles[i]
            i=i-2
        return res
        