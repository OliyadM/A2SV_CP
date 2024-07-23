class Solution:
    def maxCoins(self, piles):
        piles.sort(reverse=True)
        n = len(piles) // 3
        max_coins = 0
        
        for i in range(n):
            max_coins += piles[2 * i + 1]
        
        return max_coins

