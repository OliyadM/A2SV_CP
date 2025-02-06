# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        t = numBottles  
        
        while numBottles >= numExchange:
            n = numBottles // numExchange  
            r = numBottles % numExchange  
            
            t += n  
            numBottles = n + r  
        
        return t
