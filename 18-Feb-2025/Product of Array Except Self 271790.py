# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        cur=1
        r_product=[]
        product=1
        for num in nums:
            r_product.append(product)
            product=product*num
        l_product=[]
        product=1
        for num in nums[::-1]:
            l_product.append(product)
            product=product*num
        l_product=l_product[::-1]
        result=[]
        for i in range(len(nums)):
            result.append(l_product[i]*r_product[i])
        return result
