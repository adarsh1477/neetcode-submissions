class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row==0 or col==0:matrix[row][col] = 1
        
        for row in range(1,m):
            for col in range(1,n):
                matrix[row][col] = matrix[row-1][col]+matrix[row][col-1]


        return matrix[m-1][n-1]