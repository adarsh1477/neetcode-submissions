class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1 


        for i in range(1,len(nums)):
            best = 1
            for j in range(i):
                curr=1
                if nums[j]<nums[i]:
                    curr += dp[j]
                    best = max(curr,best)

            dp[i] = best


        return max(dp)