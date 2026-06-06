class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = float('inf')
        best = 0
        for right in prices:
            if right<left:
                left=right
            best = max(best,right-left)

        return best