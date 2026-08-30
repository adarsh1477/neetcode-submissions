class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return max(nums)


        first = [0]*n
        second = [0]*n

        first[0],first[1] = nums[0],max(nums[0],nums[1])
        second[1],second[2] = nums[1],max(nums[1],nums[2])


        for i in range(2,n-1):
            first[i] = max(first[i-1],nums[i]+first[i-2])

        for j in range(3,n):
            second[j] = max(second[j-1],second[j-2]+nums[j])



        return max(first[-2],second[-1])


        
