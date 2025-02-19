# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        arr=[0]*(len(s)+1)
        for shift in shifts:
            l,r,d=shift
            if d==0:
                d=-1
            arr[l]+=d
            arr[r+1]-=d
        print(arr)
        pre_sum=[]
        cur_sum=0
        for num in arr:
            cur_sum+=num
            pre_sum.append(cur_sum)
        pre_sum=pre_sum[:-1]
        print(pre_sum)
        result=""
        for i in range(len(s)):
            new_char = chr((ord(s[i]) - ord('a') + pre_sum[i]) % 26 + ord('a'))
            result+=new_char
        return result