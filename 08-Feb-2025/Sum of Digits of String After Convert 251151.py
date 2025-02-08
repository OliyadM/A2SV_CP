# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution(object):
    def getLucky(self,s, k):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        temp = ""
        for letter in s:
            value = alphabet.index(letter) + 1
            temp += str(value)
        
        for _ in range(k):
            total = 0
            for digit in temp:
                total += int(digit)
            
            temp = str(total)
        
        return int(temp)

        


