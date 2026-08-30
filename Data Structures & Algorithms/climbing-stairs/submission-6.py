class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        dp = [0]*n

        first = 1
        second = 2
        curr = 0
        for i in range(2,n):
            curr = first+second
            first = second
            second = curr


        return curr