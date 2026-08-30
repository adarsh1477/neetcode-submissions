class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[-1] = True



        for i in range(n-1,-1,-1):
            for word in wordDict:
                if len(word)+i <= n and s[i:len(word)+i] == word:
                    if dp[len(word)+i]:
                        dp[i] = dp[len(word)+i]
                        break



        return dp[0]