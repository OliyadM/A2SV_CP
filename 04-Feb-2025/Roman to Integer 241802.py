# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution(object):
    def romanToInt(self,s):
        int_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        i = 0
        n=len(s)
        while i < n:
            if i == len(s) - 1 or int_dict[s[i]] >= int_dict[s[i+1]]:
                result += int_dict[s[i]]
                i += 1
            else:
                result += int_dict[s[i+1]] - int_dict[s[i]]
                i += 2
        return result