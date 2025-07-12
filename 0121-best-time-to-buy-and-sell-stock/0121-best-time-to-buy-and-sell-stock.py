class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     N = len(prices)
    #     maxP = 0

    #     for i in range(N):
    #         for j in range(i+1, N):
    #             if prices[j] > prices[i]:
    #                 profit = prices[j] - prices[i]
    #                 maxP = max(maxP, profit)
                
    #     return maxP
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxP = 0
        buy = prices[0]

        for i in range(1, N):
            profit = prices[i] - buy
            maxP = max(maxP, profit)
            buy = min(buy, prices[i])
        
        return maxP