# def func(self, i, j, dp):
#         if i == 0 and j == 0:
#             return 1
        
#         if i < 0 or j < 0:
#             return 0
        
#         if dp[i][j] != -1:
#             return dp[i][j]
        
#         up = self.func(i -1, j, dp)
#         left = self.func(i, j-1, dp)

#         dp[i][j] = up + left
#         return dp[i][j]
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[-1 for j in range(n)] for i in range(m)]
#         return self.func(m-1,n-1, dp)
#     def func(self, i, j, dp):
#         for l in range(i):
#             for r in range(j):

#                 if l == 0 and r == 0:
#                     dp[l][r] = 1
#                     continue 
                
#                 up = 0
#                 left  =0 

#                 if l > 0:
#                     up = dp[l-1][r]
#                 if r > 0:
#                     left = dp[l][r-1]
                
#                 dp[l][r] = up + left 
            
#         return dp[i-1][j-1]

#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[-1] * n for _ in range(m)]

#         return self.func(m, n, dp) these are the memoization and tabulation solutions of this problem
class Solution:
    def func(self, i, j):
        prev = [0] * j
        curr = [0] * j

        for l in range(i):
            for r in range(j):

                if l == 0 and r == 0:
                    curr[r] = 1
                    continue 
                up = 0
                left = 0

                if l > 0:
                    up = prev[r]
                if r > 0:
                    left = curr[r - 1]

                curr[r] = up + left

            prev = curr

        return prev[-1]
    def uniquePaths(self, m: int, n: int) -> int:
        return self.func(m, n)