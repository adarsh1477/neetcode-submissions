class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        prefix,suffix = [],[]
        p,s = 1,1
        for i in range(n):
            p *= nums[i]
            prefix.append(p)

        for i in range(n-1,-1,-1):
            s *= nums[i]
            suffix.append(s)

        suffix = suffix[::-1]
        for i in range(n):
            if i==0:
                result[i] = suffix[i+1]
            elif i == n-1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1]*suffix[i+1]


        return result
