class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels_set = set('aeiouAEIOU')
        char_list = list(s)
        start, end = 0, len(s) - 1
        
        while start < end:
            if char_list[start] not in vowels_set:
                start += 1
            elif char_list[end] not in vowels_set:
                end -= 1
            else:
                char_list[start], char_list[end] = char_list[end], char_list[start]
                start += 1
                end -= 1
        
    
        reversed_vowels_string = ""
        for char in char_list:
            reversed_vowels_string += char
