class Solution(object):
    def commonChars(self, words):
        min_frequency = [float('inf')] * 26
        
        for word in words:
            frequency = [0] * 26
            
            for char in word:
                frequency[ord(char) - ord('a')] += 1
            
            for i in range(26):
                min_frequency[i] = min(min_frequency[i], frequency[i])
        
        result = []
        for i in range(26):
            if min_frequency[i] > 0:
                result.extend([chr(i + ord('a'))] * min_frequency[i])
        
        return result
