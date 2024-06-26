class Solution(object):
    def freqAlphabets(self, s):
        result = ""
        idx = 0
        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == '#':
                result += chr(int(s[idx:idx + 2]) + 96)
                idx += 3
            else:
                result += chr(int(s[idx]) + 96)
                idx += 1
        return result
