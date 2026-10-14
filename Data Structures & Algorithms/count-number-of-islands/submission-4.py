class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        islands = 0


        def island_count(row,col):
            if row < 0 or row >=m or col < 0 or col >=n or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"

                island_count(row+1,col)
                island_count(row-1,col)
                island_count(row,col+1)
                island_count(row,col-1)

        



        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    island_count(row,col)
                    islands += 1


        


        return islands


