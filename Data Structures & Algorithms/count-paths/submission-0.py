class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cells=[[0]*n for _ in range(m)]
        cells[0][0]=1

        for row in range(m):
            for col in range(n):

                if row==0 and col==0:
                    continue
                elif row==0:
                    cells[row][col] = 0 + cells[row][col-1]
                elif col==0:
                    cells[row][col] = 0 + cells[row-1][col]
                else:
                    cells[row][col] = cells[row][col-1] + cells[row-1][col]


        return cells[m-1][n-1]