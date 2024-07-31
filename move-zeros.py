class Solution(object):
    def moveZeroes(self, nums):
        holder = 0
        seeker = 0
        n = len(nums)
        while seeker < n:
            if nums[seeker]!=0:
                nums[seeker],nums[holder] = nums[holder],nums[seeker]
                holder+=1
            seeker+=1
        return nums
                
        
