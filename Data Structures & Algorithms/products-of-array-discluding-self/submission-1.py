class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        suffix=[]
        left,right = 1,1
        n = len(nums)
        final =[0]*len(nums)

        for i in range(n):
            left = left*nums[i]
            right = right*nums[(n-1)-i]

            prefix.append(left)
            suffix.append(right)

        suffix = suffix[::-1]


        for i in range(len(nums)):
            if i==0:
                final[i] = suffix[i+1]
            elif i==len(final)-1:
                final[i] = prefix[i-1]
            else:
                final[i] = prefix[i-1]*suffix[i+1]


        
        return final
        