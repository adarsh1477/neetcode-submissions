from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()
        m,n = len(grid),len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))


        while q:
            i,j = q.popleft()
            for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if r>=0 and r<m and c>=0 and c<n and grid[r][c] != -1 and (r,c) not in visited:
                    grid[r][c] = grid[i][j]+1
                    q.append((r,c))
                    visited.add((r,c))


