from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights),len(heights[0])
        a,p = deque(),deque()
        a_seen,p_seen = set(),set()


        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0 and (row,col) not in p_seen:
                    p.append((row,col))
                    p_seen.add((row,col))
                if row == m-1 or col == n-1 and (row,col) not in a_seen:
                    a.append((row,col))
                    a_seen.add((row,col))

        print(a)
        def flow(q,seen):
            while q:
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        q.append((r,c))
                        seen.add((r,c))


        flow(a,a_seen)
        flow(p,p_seen)

        return list(p_seen.intersection(a_seen))

