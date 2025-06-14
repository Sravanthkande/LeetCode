import heapq

class Solution:
    delRow = [-1, 0, 1, 0]
    delCol = [0, 1, 0, -1]
    def isValid(self, i, j, n, m):
        if i < 0 or i >= n:
            return False 
        if j < 0 or j >= m:
            return False 
        return True 

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        maxDiff = [[float('inf')] * m for _ in range(n)]

        maxDiff[0][0] = 0

        pq = []

        heapq.heappush(pq, (0, 0, 0))

        while pq:
            diff, row, col = heapq.heappop(pq)

            if (row, col) == (n-1, m-1):
                return diff 
            
            for i in range(4):
                nRow = row + self.delRow[i]
                nCol = col + self.delCol[i]

                if self.isValid(nRow, nCol, n, m):
                    currDiff = abs(heights[nRow][nCol] - heights[row][col])

                    if(max(currDiff, diff) < maxDiff[nRow][nCol]):
                        maxDiff[nRow][nCol] = max(currDiff, diff)
                        heapq.heappush(pq, (max(currDiff, diff), nRow, nCol))
                    
        return -1