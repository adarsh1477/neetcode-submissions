class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums2=set(nums)
        best=0
        for i in nums2:
            count=1
            if i-1 not in nums2:
                while i+1 in nums2:
                    count += 1
                    i=i+1
                best=max(best,count)
        
        return best