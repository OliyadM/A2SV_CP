# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
   def numRescueBoats(self,people, limit):
        people.sort()
        n=len(people)
        left,right=0,n-1
        count=0
    
        while left<=right :
            if right == left:
                return count+1
            if people[left] +people[right]<=limit:
                left+=1
            count+=1
            right-=1
        return count
