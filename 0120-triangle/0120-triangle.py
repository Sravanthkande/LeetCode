class Solution:
    def func(self, i, j, grid, N, dp):
        if i == N - 1:
            return grid[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        down = grid[i][j] + self.func(i + 1, j, grid, N, dp)
        diagonal = grid[i][j] + self.func(i + 1, j + 1, grid, N, dp)

        dp[i][j] = min(down, diagonal)
        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        dp = [[-1] * N for _ in range(N)]
        return self.func(0, 0, triangle, N, dp)