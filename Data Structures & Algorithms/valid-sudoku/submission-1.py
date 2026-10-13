class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n = len(board),len(board[0])
        

        for row in range(m):
            seen_row = set()
            for col in range(n):
                if board[row][col] in seen_row:
                    return False
                if board[row][col] != ".":
                    seen_row.add(board[row][col])

        for col in range(n):
            seen_col = set()
            for row in range(m):
                if board[row][col] in seen_col:
                    return False
                if board[row][col] != ".":
                    seen_col.add(board[row][col])

        
        for r,c in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
            seen_block = set()
            for row in range(r,r+3):
                for col in range(c,c+3):
                    if board[row][col] in seen_block:
                        return False
                    if board[row][col] != ".":
                        seen_block.add(board[row][col])


        return True