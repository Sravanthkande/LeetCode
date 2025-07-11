class Solution:
    # def func(self, i, j, grid, N, dp):
    #     if i == N - 1:
    #         return grid[i][j]
        
    #     if dp[i][j] != -1:
    #         return dp[i][j]
        
    #     down = grid[i][j] + self.func(i + 1, j, grid, N, dp)
    #     diagonal = grid[i][j] + self.func(i + 1, j + 1, grid, N, dp)

    #     dp[i][j] = min(down, diagonal)
    #     return dp[i][j] this is memoization approach using TC-O(N), SC-O(N) + O(N * N)

    # def func(self, i, j, grid, N, dp):
    #     for j in range(N):
    #         dp[N-1][j] = grid[N-1][j]
        
    #     for i in range(N -2, -1, -1):
    #         for j in range(i + 1):

    #             down = grid[i][j] + dp[i+1][j]
    #             diagonal = grid[i][j] + dp[i+1][j+1]

    #             dp[i][j] = min(down, diagonal)
            
    #     return dp[0][0]
    
    #this is tabulation approach using TC-O(N*N), SC-O(N*N)

    def func(self, grid, N):
        front = [0] * N 
        cur = [0] * N

        for j in range(N):
            front[j] = grid[N-1][j]
        
        for i in range(N-2, -1, -1):
            for j in range(i + 1):

                down = grid[i][j] + front[j]
                diagonal = grid[i][j] + front[j + 1]

                cur[j] = min(down, diagonal)
            
            front = cur[:]
        
        return front[0]

    #This is optimized approach using TC-O(N * N), SC-O(N) + O(N)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        return self.func(triangle, N)