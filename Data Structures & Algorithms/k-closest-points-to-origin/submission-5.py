import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for point in points:
            d = point[0]**2 + point[1]**2

            if len(heap) >= k and -heap[0][0] > d:
                heapq.heappop(heap)

            if len(heap) < k:
                heapq.heappush(heap,(-d,point))


        return [p for _,p in heap]