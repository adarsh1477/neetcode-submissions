class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}


        for i in range(len(nums)):
            check = target-nums[i]

            if check in complement:
                return[complement[check],i]

            complement[nums[i]] = i


        