class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            cmp = target - nums[i]
            if cmp in check:
                return [check[cmp],i]
            if nums[i] not in check:
                check[nums[i]]=i
        