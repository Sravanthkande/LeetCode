class Solution {
    int MOD = (int) 1e9 + 7;

    private int func(int[] coins, int ind, int target, int[][] dp){
        if(ind == 0){
            if (target % coins[0] == 0){
                return target / coins[0];
            }else{
                return (int)1e9;
            }
        }

        if(dp[ind][target] != -1){
            return dp[ind][target];
        }
        int notPick = func(coins, ind - 1, target, dp);
        int pick = (int)1e9;
        if(coins[ind] <= target){
            pick = 1 + func(coins, ind, target - coins[ind], dp);
        }
        dp[ind][target] = Math.min(notPick, pick);
        return dp[ind][target];
    }
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp = new int[n][amount + 1];
        for(int[] row : dp){
            Arrays.fill(row, -1);
        }
        int ans = func(coins, n-1, amount, dp);

        if(ans >= (int)1e9){
            return -1;
        }
        return ans;
    }
}