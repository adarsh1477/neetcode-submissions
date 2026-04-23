class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        track = set(nums)
        best = 0

        for num in nums:
            if num-1 not in track:
                count=1
                curr = num
                while curr+1 in track:
                    count+=1
                    curr = curr+1
                best = max(best,count)


        return best