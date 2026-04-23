class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        best=0
        for i in prices[1:]:
            if prices[right]<prices[left]:
                left=right
            best=max(best,prices[right]-prices[left])
            right=right+1

        return best
        