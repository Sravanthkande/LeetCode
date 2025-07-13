class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0

        for i in range(len(prices) -1, -1, -1):
            curBuy = max(-prices[i] + sell, buy)
            curSell = max(prices[i] + buy, sell)

            buy, sell = curBuy, curSell
        
        return buy