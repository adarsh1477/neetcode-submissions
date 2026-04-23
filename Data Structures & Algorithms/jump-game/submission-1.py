class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for i in range(len(nums)):
            furthest = max(furthest,i+nums[i])
            if furthest >= len(nums)-1:
                return True
            if furthest <= i+nums[i] and nums[i]==0:
                return False

        return False
