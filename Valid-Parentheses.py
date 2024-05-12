class Solution(object):
    def isValid(self, s):
        bracket_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in bracket_pairs.keys():
                stack.append(i)
            elif i in bracket_pairs.values():
                if not stack or bracket_pairs[stack.pop()] != i:
                    return False
        return len(stack) == 0
