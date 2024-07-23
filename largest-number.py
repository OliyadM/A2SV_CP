class Solution:
    def largestNumber(self, nums):
        
        nums = list(map(str, nums))
        
    
        def compare(x, y):
            return x + y > y + x
        
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if not compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        largest_num = ''.join(nums)
        
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
