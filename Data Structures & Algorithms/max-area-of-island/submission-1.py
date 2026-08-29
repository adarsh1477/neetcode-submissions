class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        best = 0


        def best_area(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                area = 1
                area += best_area(r+1,c)
                area += best_area(r-1,c)
                area += best_area(r,c+1)
                area += best_area(r,c-1)

                return area

        


        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    best = max(best,best_area(row,col))


        return best