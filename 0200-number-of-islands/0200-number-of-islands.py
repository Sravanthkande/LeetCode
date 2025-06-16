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
    def BFS(self, i, j, grid, vis):
        N = len(grid)
        M = len(grid[0])
        vis[i][j] = True
        que = deque()
        que.append((i, j))

        while que:
            row, col = que.popleft()

            for  i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                if(
                    self.isValid(nRow, nCol, N, M) and
                    grid[nRow][nCol] == '1' and
                    not vis[nRow][nCol]):

                    vis[nRow][nCol] = True
                    que.append((nRow, nCol))
                
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        vis = [[False] * M for _ in range(N)]

        count = 0

        for i in range(N):
            for j in range(M):

                if not vis[i][j] and grid[i][j] == '1':
                    count += 1
                    self.BFS(i, j, grid, vis)
                
        return count