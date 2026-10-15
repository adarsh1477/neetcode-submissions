class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return max(nums)


        

        prev = nums[0]
        curr = max(nums[0],nums[1])

        for i in range(2,n):
            temp=curr
            curr = max(nums[i]+prev,curr)
            prev=temp


        return curr