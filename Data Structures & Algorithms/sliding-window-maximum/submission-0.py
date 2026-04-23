from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = nums[0:k-1]
        q = deque(q)
        final = []

        left = 0
        right = k-1


        while right<len(nums):
            q.append(nums[right])
            final.append(max(q))
            q.popleft()
            left += 1
            right += 1
            
           


        return final