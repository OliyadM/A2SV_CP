class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()  # Ensure the list is sorted
        left = 0
        right = len(skill) - 1
        target_sum = skill[left] + skill[right] 
        
        chemistry = 0
        
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return chemistry
