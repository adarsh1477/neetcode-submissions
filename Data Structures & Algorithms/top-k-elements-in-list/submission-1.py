import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        final=[]

        for key,val in count.items():
            heapq.heappush(heap,(-val,key))

        for _ in range(k):
            v,k = heapq.heappop(heap)
            final.append(k)

        return final

