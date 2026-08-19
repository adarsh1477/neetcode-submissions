class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        size = m*n


        left = 0
        right = size-1

        while left<=right:
            mid = (left+right)//2
            row = mid//n
            col = mid%n
            print(row,col)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid-1
            else:
                left = mid+1
        
        return False


