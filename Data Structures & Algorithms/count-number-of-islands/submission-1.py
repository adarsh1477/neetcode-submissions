class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0


        def islands(r,c):

            if r<0 or r>=m or c<0 or c>=n or grid[r][c] == "0":
                return
            else:
                grid[r][c] = "0"
                islands(r+1,c)
                islands(r-1,c)
                islands(r,c+1)
                islands(r,c-1)






        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count+=1
                    islands(row,col)


        return count