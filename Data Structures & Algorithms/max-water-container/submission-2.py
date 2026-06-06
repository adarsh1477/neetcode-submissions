class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        best = 0


        while left<right:
            area = min(heights[left], heights[right]) * (right-left)
            best = max(area,best)

            if heights[left]<=heights[right]:
                left += 1
            else:
                right -= 1 

        return best