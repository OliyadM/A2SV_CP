# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        target=Counter(s1)
        window=Counter(s2[:len(s1)])
        left=0
        
        for right in range(len(s1),len(s2)):
            if target == window:
                return True
            window[s2[right]]+=1
            window[s2[left]]-=1 

            if window[s2[left]]==0:
                del window[s2[left]]
            left+=1
        if window == target:
            return True
        return False