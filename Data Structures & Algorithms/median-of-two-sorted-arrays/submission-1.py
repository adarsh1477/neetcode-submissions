class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1

        
        total_size = len(smaller)+len(larger)
        size = (total_size+1)//2
        left = 0
        right = len(smaller)

        while left<=right:
            x = (left+right)//2
            y = size-x

            l1 = float('-inf') if x==0 else smaller[x-1]
            r1 = float('inf') if x==len(smaller) else smaller[x]
            l2 = float('-inf') if y==0 else larger[y-1]
            r2 = float('inf') if y==len(larger) else larger[y]

            if l1<=r2 and l2<=r1:
                if total_size%2 != 0:
                    return max(l1,l2)
                else:
                    return(max(l1,l2)+min(r1,r2))/2

            elif l1>r2:
                right = x-1
            else:
                left = x+1

