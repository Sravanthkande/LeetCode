# def func(self, N, M, grid, dp):
#         for l in range(N):
#             for r in range(M):

#                 if grid[l][r] == 1:
#                     dp[l][r] = 0
#                     continue 
                
#                 if l == 0 and r == 0:
#                     dp[l][r] = 1
#                     continue 
                
#                 up = 0
#                 left = 0

#                 if l > 0:
#                     up = dp[l-1][r]
#                 if r > 0:
#                     left = dp[l][r-1]
                
#                 dp[l][r] = up + left 
            
#         return dp[N-1][M-1]
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         N = len(obstacleGrid)
#         M = len(obstacleGrid[0])

#         dp = [[0] * M for _ in range(N)]
#         return self.func(N-1, M-1, obstacleGrid, dp)
#     def func(self, N, M, grid, dp):
#         for l in range(N):
#             for r in range(M):

#                 if grid[l][r] == 1:
#                     dp[l][r] = 0
#                     continue 
                
#                 if l == 0 and r == 0:
#                     dp[l][r] = 1
#                     continue 
                
#                 up = 0
#                 left = 0

#                 if l > 0:
#                     up = dp[l-1][r]
#                 if r > 0:
#                     left = dp[l][r-1]
                
#                 dp[l][r] = up + left 
            
#         return dp[N-1][M-1]
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         N = len(obstacleGrid)
#         M = len(obstacleGrid[0])

#         dp = [[0] * M for _ in range(N)]
#         return self.func(N, M, obstacleGrid, dp) these are the memoization and tabulation Solutions of this problem
class Solution:
    def func(self, N, M, grid):
        prev = [0] * M
        curr = [0] * M 

        for l in range(N):
            for r in range(M):

                if grid[l][r] == 1:
                    curr[r] = 0
                    continue 
                
                if l == 0 and r == 0:
                    curr[r] = 1
                    continue 
                
                up  = 0
                left = 0

                if l > 0:
                    up = prev[r]
                if r > 0:
                    left = curr[r -1]
                
                curr[r] = up + left 
            
            prev = curr[:]
        
        return prev[M- 1]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N = len(obstacleGrid)
        M = len(obstacleGrid[0])

        return self.func(N, M, obstacleGrid)