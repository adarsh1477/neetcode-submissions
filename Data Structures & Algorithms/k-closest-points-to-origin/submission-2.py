import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            value = -(i*i + j*j)
            heapq.heappush(heap,[value,(i,j)])

            if len(heap) > k:
                    heapq.heappop(heap)
          
        return [point for (_, point) in heap]