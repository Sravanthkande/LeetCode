from collections import deque

class Solution:
    def __init__(self):
        self.delRow = [-1, 0, 1, 0]
        self.delCol = [0, 1, 0, -1]
    
    def isValid(self, i, j, N, M):
        if i < 0 or  i >= N:
            return False
        if j < 0 or j >= M:
            return False 
        
        return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        time = 0
        total = 0
        count = 0
        
        que = deque()

        for i in range(N):
            for j in range(M):

                if grid[i][j] != 0:
                    total += 1
                
                if grid[i][j] == 2:
                    que.append((i, j))
        while que:
            k = len(que)

            count += k

            for _ in range(k):
                row, col = que.popleft()
                for i in range(4):
                    nRow = row + self.delRow[i]
                    nCol = col + self.delCol[i]

                    if(
                        self.isValid(nRow, nCol, N, M) and
                        grid[nRow][nCol] == 1
                    ):
                        grid[nRow][nCol] = 2
                        que.append((nRow, nCol))
                    
            if que:
                time += 1
        if total == count:
            return time
        
        return -1