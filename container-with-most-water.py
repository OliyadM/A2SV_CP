class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        maximum_area = 0
        
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            
            if height[left_pointer] < height[right_pointer]:
                current_area = height[left_pointer] * width
                left_pointer += 1
            else:
                current_area = height[right_pointer] * width
                right_pointer -= 1
            
            maximum_area = max(maximum_area, current_area)
        
        return maximum_area
