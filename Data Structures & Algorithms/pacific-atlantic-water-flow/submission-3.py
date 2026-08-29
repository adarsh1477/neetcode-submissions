from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        a,p = deque(),deque()
        a_seen,p_seen = set(),set()


        for row in range(m):
            for col in range(n):
                if (row == 0 or col == 0) and (row,col) not in p_seen:
                    p.append((row,col))
                    p_seen.add((row,col))
                if (row == m-1 or col == n-1) and (row,col) not in a_seen:
                    a.append((row,col))
                    a_seen.add((row,col))



        

        def bfs(q,seen):
            while q:
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and (r,c) not in seen and heights[r][c] >= heights[i][j]:
                        q.append((r,c))
                        seen.add((r,c))





        

        bfs(p,p_seen)
        bfs(a,a_seen)


        return list(a_seen.intersection(p_seen))