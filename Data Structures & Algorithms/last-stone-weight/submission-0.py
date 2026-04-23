import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1 

        heapq.heapify(stones)

        while len(stones)>1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            aft_dest = stone1-stone2

            heapq.heappush(stones, -aft_dest)

        if len(stones)!=0:
            return abs(stones[0])
        return 0
