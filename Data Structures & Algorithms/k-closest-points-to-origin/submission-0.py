import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        final=[]
        for i,j in points:
            value = math.sqrt(pow(i,2) + pow(j,2))
            heapq.heappush(heap,[value,(i,j)])

        for _ in range(k):
            closest = heapq.heappop(heap)
            final.append(closest[1])

        return final