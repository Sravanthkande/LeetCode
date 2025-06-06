from typing import List

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    def isValid(self, i, j, N, M):
        return 0 <= i < N and 0 <= j < M
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        M = len(mat[0])
        
        dist = [[float('inf') for _ in range(M)] for _ in range(N)]
        que = deque()

        # Initialize queue with all zero cells
        for i in range(N):
            for j in range(M):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    que.append((i, j))
        
        # BFS to update distances
        while que:
            row, col = que.popleft()
            
            for i in range(4):
                nRow, nCol = row + self.delRow[i], col + self.delCol[i]
                
                if self.isValid(nRow, nCol, N, M) and dist[nRow][nCol] > dist[row][col] + 1:
                    dist[nRow][nCol] = dist[row][col] + 1
                    que.append((nRow, nCol))
        
        return dist