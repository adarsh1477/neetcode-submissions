class Solution:
    def climbStairs(self, n: int) -> int:
        cache={1:1,2:2}

        def steps(num):
            if num in cache:
                return cache[num]
            
            else:
                cache[num] = steps(num-2) + steps(num-1)
                return cache[num]

        

        return steps(n)