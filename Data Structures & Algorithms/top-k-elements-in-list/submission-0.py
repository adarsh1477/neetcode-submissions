import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final=[]
        counter = Counter(nums)
        bucket = [None]*(len(nums)+1)

        for key,val in counter.items():
            if bucket[val] is not None:
                bucket[val].append(key)
            else:
                bucket[val]=[key]

        for group in bucket[::-1]:
            if group is not None:
                for num in group:
                    final.append(num)
                if len(final)==k:
                    return final