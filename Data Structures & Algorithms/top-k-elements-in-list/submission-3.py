from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key,val in freq.items():
            if len(heap)>=k and heap[0][0] < val:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap,(val,key))


        return [i[1] for i in heap]