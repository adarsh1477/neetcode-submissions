class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0]*(amount+1)

        for i in range(1,amount+1):
            least = float('inf')
            for coin in coins:
                diff = i-coin
                if diff<0:
                    break
                least=min(least,dp[diff]+1)

            dp[i] = least

        
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1                


        