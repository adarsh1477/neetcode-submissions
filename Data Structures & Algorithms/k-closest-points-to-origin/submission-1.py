import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i,j in points:
            value = -(math.sqrt(pow(i,2) + pow(j,2)))
            heapq.heappush(heap,[value,(i,j)])

            if len(heap) > k:
                    heapq.heappop(heap)
          
        result=[]
        for value,key in heap:
            result.append(key)

        return result