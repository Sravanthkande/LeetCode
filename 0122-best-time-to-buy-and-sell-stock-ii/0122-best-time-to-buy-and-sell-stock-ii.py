class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 2 for _ in range(N + 1)]

        for ind in range(N - 1, -1, -1):
            for buy in range(2):
                if buy:
                    buyToday = -prices[ind] + dp[ind + 1][0]
                    skip = dp[ind + 1][1]
                    dp[ind][buy] = max(buyToday, skip)
                else:
                    sellToday = prices[ind] + dp[ind + 1][1]
                    skip = dp[ind + 1][0]
                    dp[ind][buy] = max(sellToday, skip)
                
        return dp[0][1]