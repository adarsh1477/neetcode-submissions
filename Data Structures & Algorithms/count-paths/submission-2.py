class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    grid[row][col] = 1
                else:
                    grid[row][col] = grid[row-1][col]+grid[row][col-1]



        return grid[m - 1][n - 1]