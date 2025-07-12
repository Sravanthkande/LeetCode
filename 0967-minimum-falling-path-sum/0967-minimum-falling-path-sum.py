class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])

        dp = [[0] * M for _ in range(N)]

        for j in range(M):
            dp[0][j] = matrix[0][j]

        for i in range(1, N):
            for j in range(M):
                down = dp[i-1][j]
                left = dp[i-1][j-1] if j - 1 >= 0 else float('inf')
                right = dp[i-1][j+1] if j + 1 < M else float('inf')

                dp[i][j] = matrix[i][j] + min(down, left, right)
            
        return min(dp[N-1])