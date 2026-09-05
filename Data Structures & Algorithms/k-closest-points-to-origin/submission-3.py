import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []
        for point in points:
            dist = (point[0]**2) + (point[1]**2)

            if len(heap) >=k and -heap[0][0] > dist:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap,(-dist,point))


        for d,p in heap:
            result.append(p)


        return result