class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        prefix,suffix = [],[]
        p=1
        for i in range(n):
            result[i] = p
            p *= nums[i]
        s=1
        for i in range(n-1,-1,-1):
            result[i] *= s
            s *= nums[i]
            
        return result      