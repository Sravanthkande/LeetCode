class Solution:
    def func(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[0][0]
        
        if i < 0 or j < 0:
            return int(1e9)
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = grid[i][j] + self.func(i-1, j, grid, dp)
        left = grid[i][j] + self.func(i, j-1, grid, dp)

        dp[i][j] = min(up, left)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        dp = [[-1 for j in range(M)] for i in range(N)]

        return self.func(N-1, M-1, grid, dp)