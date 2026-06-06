from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        final = []
        print(count)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key,val in count.items():
            bucket[val].append(key)

        print(bucket)
        for nums in bucket[::-1]:
            if nums!=[]:
                for num in nums:

                    final.append(num)
                    if len(final) == k:
                        return final