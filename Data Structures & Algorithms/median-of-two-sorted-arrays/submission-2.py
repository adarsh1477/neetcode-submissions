class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            smaller,larger = nums1,nums2
        else:
            smaller,larger = nums2,nums1


        total_size = len(smaller) + len(larger)
        left = 0
        right = len(smaller)
        half_size = (total_size+1)//2

        while left<=right:
            x = (left+right)//2
            y = half_size - x

            l1 = smaller[x-1] if x!=0 else float('-inf')
            r1 = smaller[x] if x!=len(smaller) else float('inf')
            l2 = larger[y-1] if y!=0 else float('-inf')
            r2 = larger[y] if y!=len(larger) else float('inf')

            
            

            if l1<=r2 and l2<=r1:
                if total_size%2 != 0:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2

            elif l1>r2:
                right = x-1
            else:
                left = x+1
