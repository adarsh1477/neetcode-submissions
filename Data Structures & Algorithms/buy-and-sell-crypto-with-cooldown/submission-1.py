class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n=len(prices)

        buy = [0] * (n+1)
        sell = [0] * (n+1)


        buy[1] = -prices[0]
        sell[1] = 0

        for i in range(1,len(prices)):
            buy[i+1] = max(buy[i],sell[i-1]-prices[i])
            sell[i+1] = max(sell[i],buy[i]+prices[i])


        return sell[-1]