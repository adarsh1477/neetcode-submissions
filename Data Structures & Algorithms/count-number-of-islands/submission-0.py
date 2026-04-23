class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        island_count=0


        def check_island(row,col):
            if row<0 or row>=m or col<0 or col>=n or grid[row][col]=='0':
                return
            else:
                grid[row][col]='0'
                check_island(row,col+1)
                check_island(row-1,col)
                check_island(row,col-1)
                check_island(row+1,col)


        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=='1':
                    island_count += 1
                    check_island(row,col)

        return island_count

        