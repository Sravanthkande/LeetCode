class Solution:
    def isSafe(self, row, col, board):
        r,c = row, col

        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False 
            r -= 1
            c -= 1
        
        r, c = row, col
        while c >= 0:
            if board[r][c] == 'Q':
                return False 
            c -= 1
        
        r, c = row, col

        while r < len(board) and c >= 0:
            if board[r][c] == 'Q':
                return False 
            r += 1
            c -=1 

        return True 
    
    def func(self, col, ans, board):
        if col == len(board):
            ans.append(list(board))
            return 
        
        for row in range(len(board)):
            if self.isSafe(row, col, board):
                board[row] = board[row][:col] + 'Q' + board[row][col +1:]
                self.func(col +1, ans, board)
                board[row] = board[row][:col] + '.' + board[row][col +1:]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ['.' * n for _ in range(n)]
        self.func(0, ans, board)
        return ans