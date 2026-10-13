class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        left = 0 
        right = n-1

        l_max,r_max = 0,0


        while left<right:
            if height[left] <= height[right]:
                l_max = max(l_max,height[left])
                total += l_max-height[left]
                left += 1
            
            else:
                r_max = max(r_max,height[right])
                total += r_max - height[right]
                right -= 1



        return total