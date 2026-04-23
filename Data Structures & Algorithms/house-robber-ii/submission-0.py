class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        size = len(nums)

        dp1=[0]*size
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        for i in range(2,size-1):
            dp1[i] = max(dp1[i-1], nums[i]+dp1[i-2])



        dp2=[0]*size
        dp2[1]=nums[1]
        dp2[2]=max(nums[1],nums[2])
        for j in range(3,size):
            dp2[j]=max(dp2[j-1], nums[j]+dp2[j-2])

        

        return max(dp1[-2],dp2[-1])



        