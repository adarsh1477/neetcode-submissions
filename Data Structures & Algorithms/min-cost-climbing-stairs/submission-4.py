class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*n

        prev = cost[0]
        curr = cost[1]

        for i in range(2,n):
            temp = curr
            curr = min(prev,curr)+cost[i]
            prev = temp


        return min(prev,curr)
        