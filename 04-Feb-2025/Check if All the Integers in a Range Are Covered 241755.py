# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution(object):
    def isCovered(self, ranges, left, right):
        target_set={num for num in range(left,right+1)}
        large_set=set()
        for rangg in ranges:
            temp_nums={num for num in range(rangg[0],rangg[1]+1)}
            large_set  = large_set.union(temp_nums)
        print(target_set)
        print(large_set)
        return target_set<=large_set