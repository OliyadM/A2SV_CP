# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins < cost:
                return count
            coins -= cost
            count += 1
        return count
