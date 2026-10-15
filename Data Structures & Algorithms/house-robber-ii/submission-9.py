class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return max(nums)

        prev1,curr1 = nums[0],max(nums[0],nums[1])
        
        for i in range(2,n-1):
            temp = curr1
            curr1 = max(nums[i]+prev1,curr1)
            prev1 = temp

        prev2,curr2 = nums[1],max(nums[1],nums[2])
        
        for i in range(3,n):
            temp = curr2
            curr2 = max(nums[i]+prev2,curr2)
            prev2 = temp


        return max(curr1,curr2)


        

        
