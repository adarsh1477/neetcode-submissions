class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n = len(board),len(board[0])

        for i in range(m):
            seen = set()
            for j in range(n):
                num = board[i][j]
                if num in seen:
                    return False
                elif num!=".":
                    seen.add(num)

        for i in range(m):
            seen = set()
            for j in range(n):
                num = board[j][i]
                if num in seen:
                    return False
                elif num!=".":
                    seen.add(num)

        
        start = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]


        for i,j in start:
            seen = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    num = board[row][col]
                    if num in seen:
                        return False
                    elif num!=".":
                        seen.add(num)


        return True









