from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_queue = deque()
        p_seen = set()
        a_queue = deque()
        a_seen = set()

        m,n = len(heights),len(heights[0])



        for col in range(n):
            p_queue.append([0,col])
            p_seen.add((0,col))


        for row in range(1,m):
            p_queue.append([row,0])
            p_seen.add((row,0))


        for col in range(n):
            a_queue.append([m-1,col])
            a_seen.add((m-1,col))

        for row in range(m-1):
            a_queue.append([row,n-1])
            a_seen.add((row,n-1)) 


        def overflow(q,seen):
            while q:
                i,j = q.popleft()
                for row,col in ([0,1],[1,0],[-1,0],[0,-1]):
                    r,c = i+row, j+col
                    if 0<= r <m and 0<= c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        q.append([r,c])
                        seen.add((r,c))




        overflow(p_queue,p_seen)
        overflow(a_queue,a_seen)

        return list(p_seen.intersection(a_seen))