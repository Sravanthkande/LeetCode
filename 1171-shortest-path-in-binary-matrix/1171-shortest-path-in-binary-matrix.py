from collections import deque

class Solution:
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False
        if j < 0 or j >= m:
            return False 
        return True 

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[n-1][m-1]:
            return -1

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        que = deque()

        que.append((0, 0, 0))

        while que:
            dis, row, col = que.popleft()
            
            if (row, col) == (n-1, m-1):
                return dis + 1

            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    nRow = row + delRow
                    nCol = col + delCol

                    if(
                        self.isValid(nRow, nCol, n, m) and
                        grid[nRow][nCol] == 0 and
                        dis + 1 < dist[nRow][nCol]
                    ):
                        dist[nRow][nCol] = dis + 1
                        que.append((dis + 1, nRow, nCol))

        return -1