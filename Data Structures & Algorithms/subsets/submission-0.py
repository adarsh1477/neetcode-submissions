class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res,sol = [],[]

        def backtrack(level):
            if level == len(nums):
                res.append(sol[:])
                return

            backtrack(level+1)

            sol.append(nums[level])

            backtrack(level+1)
            sol.pop()
        

        backtrack(0)
        return res
        
        