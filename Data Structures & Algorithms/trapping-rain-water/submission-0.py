class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = [],[]
        n = len(height)
        left.append(0)
        right.append(0)
        water = 0
        l_max = 0
        for i in height:
            l_max = max(l_max,i)
            left.append(l_max)

        r_max=0
        for j in height[::-1]:
            r_max = max(j,r_max)
            right.append(r_max)
        right=right[::-1]


        pott = 0
        for i in range(1,n):
            pott = min(left[i],right[i])
            pott = pott - height[i]
            if pott > 0:
                water += pott

        return water