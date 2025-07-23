class Solution {
    // int MOD = (int) 1e9 + 7;

    // private int func(int[] coins, int ind, int target, int[][] dp){
    //     if(ind == 0){
    //         if (target % coins[0] == 0){
    //             return target / coins[0];
    //         }else{
    //             return (int)1e9;
    //         }
    //     }

    //     if(dp[ind][target] != -1){
    //         return dp[ind][target];
    //     }
    //     int notPick = func(coins, ind - 1, target, dp);
    //     int pick = (int)1e9;
    //     if(coins[ind] <= target){
    //         pick = 1 + func(coins, ind, target - coins[ind], dp);
    //     }
    //     dp[ind][target] = Math.min(notPick, pick);
    //     return dp[ind][target];
    // } this memoization solution TC-O(N * target) SC-O(N*target) + O(N)
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp = new int[n][amount + 1];

        for(int i = 0; i <= amount; i++){
            if(i % coins[0] == 0){
                dp[0][i] = i / coins[0];
            }else{
                dp[0][i] = (int)1e9;
            }
        }

        for(int ind = 1; ind < n; ind++){
            for(int target = 0; target <= amount; target++){
                int notPick = dp[ind - 1][target];

                int pick = (int)1e9;
                if(coins[ind] <= target){
                    pick = 1 + dp[ind][target - coins[ind]];
                }

                dp[ind][target] = Math.min(notPick, pick);
            }
        }

        int ans = dp[n-1][amount];
        if(ans >= (int)1e9){
            return -1;
        }

        return ans;
    }
    // this is tabulation solution TC-O(N * target) , SC-O(N*target)
}