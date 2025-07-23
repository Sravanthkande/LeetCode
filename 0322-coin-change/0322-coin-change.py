class Solution:
    # MOD = int(1e9) + 7
    # def func(self, arr, ind, target, dp):
    #     if(ind == 0):
    #         if target % arr[0] == 0:
    #             return target // arr[0]
    #         else:
    #             return int(1e9) + 7 
    #     if dp[ind][target] != -1:
    #         return dp[ind][target]

    #     notPick = self.func(arr, ind-1, target,dp)
    #     pick = int(1e9)
    #     if(arr[ind] <= target):
    #         pick = 1 + self.func(arr, ind, target - arr[ind], dp)
        
    #     dp[ind][target] = min(notPick, pick)
    #     return dp[ind][target] this is memoization solution usign TC-O(N*target), SC-O(N*target) + O(N)
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = int(1e9)

        for i in range(1, n):
            for j in range(amount + 1):
                notPick = dp[i -1][j]
                pick = int(1e9)
                if coins[i] <= j:
                    pick =  1 + dp[i][j-coins[i]]
                
                dp[i][j] = min(notPick, pick)
            
        ans = dp[n-1][amount]
        if ans >= int(1e9):
            return -1
        
        return ans