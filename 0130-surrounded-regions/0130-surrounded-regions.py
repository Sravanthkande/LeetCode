class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    def isValid(self, i, j, N, M):
        if i < 0 or i >= N:
            return False 
        if j < 0 or j >= M:
            return False 
        
        return True 

    def DFS(self, row, col, vis, mat, N, M):
        #mark row and col coordinates as visited
        vis[row][col] = True 

        #Check for the 4 neighbours
        for i in range(4):
            nRow = row + self.delRow[i]
            nCol = col + self.delCol[i]

            #If an unvisited, valid vell contains 'O'
            if(
                self.isValid(nRow, nCol, N, M) and
                mat[nRow][nCol] == 'O' and
                not vis[nRow][nCol]
            ):  
                #Recursive DFS traversal
                self.DFS(nRow, nCol, vis, mat, N, M)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        M = len(board[0])

        vis = [[False] * M for _ in range(N)]

        #Traverse for boundary 'O' s

        #Traverse for row boundary
        for j in range(M):

            #First row
            if not vis[0][j] and board[0][j] == 'O':
                self.DFS(0, j, vis, board, N, M)
            #Last row 
            if not vis[N-1][j] and board[N-1][j] == 'O':
                self.DFS(N-1, j, vis, board, N, M)
        
        #Traverse for boundary column
        for i in range(N):
            #first Column
            if not vis[i][0] and board[i][0] == 'O':
                self.DFS(i, 0, vis, board, N, M)
            #last Column
            if not vis[i][M-1] and board[i][M-1] == 'O':
                self.DFS(i, M-1, vis, board, N, M)
        
        #Traverse the board and convert unvisited O's to X 
        for i in range(N):
            for j in range(M):

                if(
                    board[i][j] == 'O' and
                    not vis[i][j]
                ):
                    board[i][j] = 'X'
        return board