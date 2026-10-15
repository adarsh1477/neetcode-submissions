import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap,-stone)


        while len(heap)>1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)

            val = s1-s2
            if val!=0:
                heapq.heappush(heap,-val)


        return -heap[0] if len(heap) == 1 else 0