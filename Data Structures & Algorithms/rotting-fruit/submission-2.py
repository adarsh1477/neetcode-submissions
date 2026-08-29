from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q=deque()
        fresh = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1: fresh +=1
                elif grid[row][col] == 2:
                    q.append((row,col))


        if fresh == 0:
            return 0


        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1


        return minutes if fresh == 0 else -1
