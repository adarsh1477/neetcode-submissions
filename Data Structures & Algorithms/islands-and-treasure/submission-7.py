from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited,q = set(),deque()
        m,n = len(grid),len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))


        

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and (r,c) not in visited and grid[r][c]!=-1:
                        grid[r][c] = grid[i][j] + 1
                        q.append((r,c))
                        visited.add((r,c))



        

