from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [None]*(len(nums)+1)
        result = []


        for key,val in freq.items():

            if bucket[val] == None:
                bucket[val] = []
            bucket[val].append(key)


        for i in range(len(bucket)-1,-1,-1):
            if bucket[i] != None:
                for num in bucket[i]:
                    result.append(num)
                    if len(result) == k:
                        return result