class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        best=0


        def area_island(row,col):
            if row<0 or row>=m or col<0 or col>=n or grid[row][col]==0:
                return 0
            else:
                grid[row][col]=0
                area=1
                area += area_island(row,col+1)
                area += area_island(row-1,col)
                area += area_island(row,col-1)
                area += area_island(row+1,col)

                return area



        
        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    area = area_island(row,col)
                    best=max(best,area)



        
        return best
        