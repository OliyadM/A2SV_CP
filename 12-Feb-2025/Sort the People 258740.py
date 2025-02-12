# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):
        n=len(names)
        for _ in range(n):
            for i in range(n-1):
                if heights[i+1]>heights[i]:
                    heights[i],heights[i+1]=heights[i+1],heights[i]
                    names[i],names[i+1]=names[i+1],names[i]
        return names