# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        n=len(s)
        array=[""]*n
        for i,indice in enumerate(indices):
            array[indice] = s[i]
        shuffled=''
        for i in array:
            shuffled+=i
        return shuffled
        