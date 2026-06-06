class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left<right:
                total = nums[left]+nums[i]+nums[right]

                if total == 0:
                    final.append([nums[left],nums[i],nums[right]])
                    left = left+1
                    right = right-1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -=1
                elif total<0:
                    left += 1
                else:
                    right -=1

        return final