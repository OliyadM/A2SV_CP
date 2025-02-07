# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        dect=defaultdict(list)
        for word in strs:
            dect[tuple(sorted(word))].append(word)
        return list(dect.values())
