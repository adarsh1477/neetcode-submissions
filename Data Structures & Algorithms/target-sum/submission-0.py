class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        
        def dp(i,total):

            if i == len(nums):
                return 1 if total == target else 0
            
            return dp(i+1,total+nums[i]) + dp(i+1,total-nums[i])








        return dp(0,0)