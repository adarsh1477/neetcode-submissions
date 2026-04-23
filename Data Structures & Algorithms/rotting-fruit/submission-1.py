from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0
        for row in range (m):
            for col in range(n):
                if grid[row][col]==2:
                    q.append((row,col))
                elif grid[row][col]==1:
                    fresh += 1
                
        if fresh==0:
            return fresh
        minutes=-1
        while q:
            size=len(q)
            minutes += 1
            for i in range(size):
                row,col = q.popleft()
                for r,c in [(row,col+1),(row+1,col),(row,col-1),(row-1,col)]:
                    if 0<= r < m and 0 <= c < n and grid[r][c]==1:
                        grid[r][c]=2
                        fresh -= 1
                        q.append((r,c))

        if fresh == 0:
            return minutes

        else:
            return -1
        