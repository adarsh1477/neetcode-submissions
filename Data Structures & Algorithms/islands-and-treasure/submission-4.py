from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        m=len(grid)
        n=len(grid[0])
        q_seen=set()


        for row in range(m):
            for col in range(n):
                if grid[row][col]==0:
                    q.append((row,col))
                    q_seen.add((row,col))


        while q:
            i,j = q.popleft()
            for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=r<m and 0<=c<n and (r,c) not in q_seen and grid[r][c]!=-1:
                    grid[r][c] = min(grid[r][c],grid[i][j]+1)
                    q.append((r,c))
                    q_seen.add((r,c))


        



        
