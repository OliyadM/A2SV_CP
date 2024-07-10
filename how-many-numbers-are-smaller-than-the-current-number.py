class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101  
        for num in nums:
            count[num] += 1
        
        prefix_count = [0] * 101
        for i in range(1, 101):
            prefix_count[i] = prefix_count[i-1] + count[i-1]
        
        result = []
        for num in nums:
            result.append(prefix_count[num])
        
        return result
