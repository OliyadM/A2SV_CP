# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            n, d = s.split('@')
            masked_n = n[0] + '*****' + n[-1]
            return f"{masked_n}@{d}"
        else:
            digits = [c for c in s if c.isdigit()]
            l = len(digits)
            last4 = ''.join(digits[-4:])
            cc = l - 10
            
            if cc == 0:
                return f"***-***-{last4}"
            elif cc == 1:
                return f"+*-***-***-{last4}"
            elif cc == 2:
                return f"+**-***-***-{last4}"
            elif cc == 3:
                return f"+***-***-***-{last4}"
            else:
                return f"***-***-{last4}"