class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        n = len(temperatures)

        for t in range(n-1,-1,-1):
            while stack and temperatures[t] >= temperatures[stack[-1]]:
                stack.pop()
            stack.append(t)

            if len(stack) < 2:
                result.append(0)
            else:
                result.append(stack[-2]-stack[-1])



        return result[::-1] 