class Solution:
    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     N = len(matrix)
    #     M = len(matrix[0])

    #     dp = [[0] * M for _ in range(N)]

    #     for j in range(M):
    #         dp[0][j] = matrix[0][j]
        
    #     for i in range(1, N):
    #         for j in range(M):
    #             down = dp[i-1][j]
    #             left = dp[i-1][j-1] if j-1 >= 0 else float('inf')
    #             right = dp[i-1][j+1] if j+1 < M else float('inf')

    #             dp[i][j] = matrix[i][j] + min(down, left, right)
            
    #     return min(dp[N-1]) this tabulation approach 
    
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])

        prev= matrix[0][:]

        for i in range(1, N):
            curr = [0] * M 
            for j in range(M):
                down = prev[j]
                left = prev[j-1] if j > 0 else float('inf')
                right = prev[j+1] if j < M-1 else float('inf')
                curr[j] = matrix[i][j] + min(down, left, right)
            prev = curr
        
        return min(prev)