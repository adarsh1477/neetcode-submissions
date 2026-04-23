class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        minp = nums[0]
        best = nums[0]


        for i in nums[1:]:
            max_prev = maxp
            maxp = max(i,maxp*i,minp*i)
            minp = min(i,max_prev*i,minp*i)
            best = max(best,maxp)


        return best