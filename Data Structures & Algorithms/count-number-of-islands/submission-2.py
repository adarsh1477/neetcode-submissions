class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        island_count = 0


        def island(r,c):
            if r<0 or r>=m or c<0 or c >=n or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"

                island(r+1,c)
                island(r-1,c)
                island(r,c+1)
                island(r,c-1)



        

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island(row,col)
                    island_count += 1




        return island_count