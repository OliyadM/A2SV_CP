# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        count=0
        result=[]
        for num in nums:
            if num%2==0:
                count+=num
        print(count)
        for query in queries:
            index=query[1]
            k=query[0]
            num=nums[index]
            new_num=nums[index]+k
            if nums[index] %2==0 and new_num %2!=0:
                count-=num
            elif nums[index]%2!=0 and new_num%2==0:
                count+=new_num
            elif nums[index]%2==0 and new_num%2==0:
                count+=new_num
                count-=num
            nums[index]=new_num
            result.append(count)
        return result
                    
            