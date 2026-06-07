class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)


        dp_first = [0]*n
        dp_second = [0]*n

        
        dp_first[0] = nums[0]
        dp_first[1] = max(nums[0],nums[1])
        for i in range(2,n-1):
            dp_first[i] = max(dp_first[i-1],nums[i]+dp_first[i-2])


        dp_second[1] = nums[1]
        dp_second[2] = max(nums[1],nums[2])   
        for j in range(3,n):
            dp_second[j] = max(dp_second[j-1],nums[j]+dp_second[j-2])


        return max(dp_first[n-2],dp_second[n-1])