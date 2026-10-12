class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        c = 0

        for i,num in enumerate(nums):
            c = target-num
            if c in check:
                return [check[c],i]

            check[num] = i



        