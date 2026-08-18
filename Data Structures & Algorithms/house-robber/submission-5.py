class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2: return max(nums)

        first = nums[0]
        second = max(nums[0],nums[1])


        for i in range(2,n):
            curr = max(second,nums[i]+first)
            first = second
            second = curr


        return curr