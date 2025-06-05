from collections import deque

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

    def BFS(self, grid, que, vis):
        N = len(grid)
        M = len(grid[0])

        while que:
            row, col = que.popleft()

            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                if(
                    self.isValid(nRow, nCol, N, M) and
                    grid[nRow][nCol] == 1 and
                    vis[nRow][nCol] == False
                ):
                    vis[nRow][nCol] = True 
                    que.append((nRow, nCol))
            
    def numEnclaves(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        que = deque()

        vis = [[False] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):

                if(
                    (i == 0 or i == N - 1 or j == 0 or j == M - 1) and
                    grid[i][j] == 1
                ):
                    vis[i][j] = True
                    que.append((i, j))
        self.BFS(grid, que, vis)
        count = 0

        for i in range(N):
            for j in range(M):

                if(
                    grid[i][j] == 1 and
                    vis[i][j] == False
                ):
                    count += 1
        return count