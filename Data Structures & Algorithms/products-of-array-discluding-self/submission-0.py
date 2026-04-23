class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix,final = [],[],[]

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)


        product=1
        for num in nums[::-1]:
            product *= num
            suffix.append(product)

        suffix=suffix[::-1]
            
        for i in range(len(nums)):
            if i==0:
                final.append(suffix[i+1])
            elif i==len(nums)-1:
                final.append(prefix[i-1])
            else:
                final.append(prefix[i-1]*suffix[i+1])

        return final