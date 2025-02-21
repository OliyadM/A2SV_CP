# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum={0:1}
        count=0
        run_sum=0

        for num in nums:
            run_sum+=num

            if run_sum%k<0:
                run_sum+=k

            if run_sum %k in pre_sum:
                count+=pre_sum[run_sum%k]
                pre_sum[run_sum%k]+=1
            else:
                pre_sum[run_sum%k] =1

        return count
