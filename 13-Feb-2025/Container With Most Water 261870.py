# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        maximum=0
        while left<right:
            cur_area=min(height[left],height[right])*(right-left)
            maximum=max(cur_area,maximum)
            if height[left]<height[right]:
                left+=1
            else:
               right-=1
            cur_area=min(height[left],height[right])*(right-left)
            maximum=max(cur_area,maximum)
        return maximum
            
            

          