# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self,skill):
        if not skill or not skill[1]:
            return -1
        skill.sort()
        chemistry=0
        s=skill[0]+skill[-1]
        n=len(skill)
        left,right=0,n-1
        while left<right:
            cur_sum=skill[left]+skill[right]
            if cur_sum!=s:
                return -1
            else:
                chemistry+=skill[left]*skill[right]
                left+=1
                right-=1
        return chemistry
            