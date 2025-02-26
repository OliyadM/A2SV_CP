# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a, b = 0, 0  
        res = []  
        for _ in range(len(firstList) + len(secondList)):  
            if a >= len(firstList) or b >= len(secondList):  
                break  

            s1, e1 = firstList[a]
            s2, e2 = secondList[b]
            start = max(s1, s2)  
            end = min(e1, e2)  

            if start <= end:
                res.append([start, end])
            if e1 < e2:
                a += 1
            else:
                b += 1

        return res  
