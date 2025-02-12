# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq_count = Counter(s)
        freq_sort = list(freq_count.items())
        
        def compare(value):
            return value[1]
        
        freq_sort.sort(key=compare, reverse=True)
        
        result = ''
        for char, value in freq_sort:
            result += char * value
        
        return result

