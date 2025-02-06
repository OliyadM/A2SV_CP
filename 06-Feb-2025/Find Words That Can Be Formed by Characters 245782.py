# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        char_count=Counter(chars)
        result=0
        for word in words:
            k=True
            for letter , count in Counter(word).items():
                if count>char_count[letter]:
                    k=False
            if k:
                result+=len(word)    
        return result       
            


            
                            
