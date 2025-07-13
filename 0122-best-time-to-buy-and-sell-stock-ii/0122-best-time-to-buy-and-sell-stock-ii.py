class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        def dfs(ind, buy, dp):
            if ind == N:
                return 0
            
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            
            if buy:
                buyToday = -prices[ind] + dfs(ind+1, 0, dp)
                skip = dfs(ind + 1,  1, dp)
                dp[ind][buy] = max(buyToday, skip)
            
            else:
                sellToday = prices[ind] + dfs(ind + 1, 1, dp)
                skip = dfs(ind + 1,  0, dp)
                dp[ind][buy] = max(sellToday, skip)
            
            return dp[ind][buy]
        
        dp = [[-1] * 2 for _ in range(N)]
        return dfs(0, 1, dp)