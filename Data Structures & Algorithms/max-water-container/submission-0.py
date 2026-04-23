class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        best=0
        area=0

        while left<right:
            h=min(heights[left],heights[right])
            b=right-left
            area=h*b
            best=max(best,area) 
            if heights[left]<heights[right]:
                left=left+1
            elif heights[left]>=heights[right]:
                right=right-1

        return best      