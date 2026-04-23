class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        final=0
        for numbers in nums:
            final = final^numbers

        return final
        