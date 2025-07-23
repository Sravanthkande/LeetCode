class Solution:
    MOD = int(1e9) + 7
    def func(self, arr, ind, target, dp):
        if(ind == 0):
            if target % arr[0] == 0:
                return target // arr[0]
            else:
                return int(1e9) + 7 
        if dp[ind][target] != -1:
            return dp[ind][target]

        notPick = self.func(arr, ind-1, target,dp)
        pick = int(1e9)
        if(arr[ind] <= target):
            pick = 1 + self.func(arr, ind, target - arr[ind], dp)
        
        dp[ind][target] = min(notPick, pick)
        return dp[ind][target]
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        ans = self.func(coins, n-1, amount, dp)
        if ans >= int(1e9):
            return -1
        
        return ans