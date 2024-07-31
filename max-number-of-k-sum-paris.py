class Solution:
    def maxOperations(self, nums, k):
        freq = {}
        result = 0
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in list(freq.keys()):
            comp = k - num
            if comp in freq:
                if num == comp:
                    result += freq[num] // 2
                else:
                    pairs = min(freq[num], freq[comp])
                    result += pairs
                    freq[num] -= pairs
                    freq[comp] -= pairs
        
        return result
