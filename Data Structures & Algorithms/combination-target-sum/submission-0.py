class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        

        def com(level,sum):
            if sum==target:
                res.append(sol[:])
                return

            if sum>target:
                return

            for i in range(level,len(nums)):

                sol.append(nums[i])
                com(i,sum+nums[i])
                sol.pop()
        com(0,0)
        return res
        