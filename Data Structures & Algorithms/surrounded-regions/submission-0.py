class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])


        def surround(row,col):
            if row<0 or row>=m or col<0 or col>=n or board[row][col]!="O":
                return
            else:
                board[row][col] = "S"
                surround(row+1,col)
                surround(row-1,col)
                surround(row,col+1)
                surround(row,col-1)

        def surround_final(row,col):
            if row<0 or row>=m or col<0 or col>=n or board[row][col]!="O":
                return
            else:
                board[row][col] = "X"
                surround_final(row+1,col)
                surround_final(row-1,col)
                surround_final(row,col+1)
                surround_final(row,col-1)




        for row in range(m):
            for col in range(n):
                if row==0 or col==0 or row==m-1 or col==n-1:
                    if board[row][col] == "O":
                        surround(row,col)


        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    surround_final(row,col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "S":
                    board[row][col] = "O"