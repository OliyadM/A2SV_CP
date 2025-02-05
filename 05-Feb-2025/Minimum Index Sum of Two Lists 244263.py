# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
    def findRestaurant(self, list1, list2):
        a=set(list1)
        b=set(list2)
        c=a&b
        dect=defaultdict(int)
        for string in c:
            dect[string]+=list1.index(string) +list2.index(string)
        k=min(dect.values())
        array=[]
        for key,value in dect.items():
            if value == k:
                array.append(key)
        return array

