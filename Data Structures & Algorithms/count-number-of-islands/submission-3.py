class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        islands = 0


        def count_island(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                count_island(r+1,c)
                count_island(r-1,c)
                count_island(r,c+1)
                count_island(r,c-1)



        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count_island(row,col)
                    islands += 1



        return islands