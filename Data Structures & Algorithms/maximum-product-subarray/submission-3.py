class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = best = nums[0]



        for num in nums[1:]:
            temp = maxp
            maxp = max(maxp*num,minp*num,num)
            minp = min(minp*num,temp*num,num)
            best = max(best,maxp)


        return best