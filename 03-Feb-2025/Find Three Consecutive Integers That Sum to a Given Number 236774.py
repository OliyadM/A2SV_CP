# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution(object):
    def sumOfThree(self, num):
        if (num-3) % 3 !=0:
            return []
        else:
            k=(num-3)/3
            k=int(k)
            return [k,k+1,k+2]