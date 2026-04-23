class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if all(num<0 for num in nums):
            return(max(nums))
        current=nums[0]
        best=nums[0]
        for i in nums[1:]:
            current=max(i,current+i)
            best=max(best,current)
        
        return best

