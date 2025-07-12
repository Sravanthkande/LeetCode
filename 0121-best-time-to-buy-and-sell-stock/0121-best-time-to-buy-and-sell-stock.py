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
        left, right = 0, 1
        maxP = 0

        while right < N:
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right 
            right += 1
        
        return maxP