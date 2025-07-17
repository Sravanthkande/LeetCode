class Solution:
    # def func(self, ind, nums, target, dp):
    #     if target == 0:
    #         return True 
        
    #     if ind == 0:
    #         return nums[0] == target
        
    #     if dp[ind][target] != -1:
    #         return dp[ind][target] == 1
        
    #     notTaken = self.func(ind -1, nums, target, dp)
    #     taken = False 
         
    #     if nums[ind] <= target:
    #         taken = self.func(ind -1, nums, target - nums[ind], dp)
        
    #     dp[ind][target] = 1 if notTaken or taken else 0 
    #     return dp[ind][target] == 1
    #Memoization approach using TC-O(N*target), SC-O(N*target) + O(N)

    # def func(self, nums, target):
    #     N = len(nums)
    #     dp = [[False] * (target + 1) for _ in range(N)]
    #     for i in range(N):
    #         dp[i][0] = True 
        
    #     if nums[0] <= target:
    #         dp[0][nums[0]] = True 

    #     for i in range(1, N):
    #         for j in range(1, target + 1):
    #             notTake = dp[i-1][j]
    #             take = dp[i-1][j - nums[i]] if nums[i] <= j else False 
    #             dp[i][j] = notTake or take 
            
    #     return dp[N - 1][target]
    #Tabulation approach using TC-O(N*target), SC- O(N*target).

    def func(self, nums, target):
        dp = [False] * (target + 1)
        dp[0] = True 

        if nums[0] <= target:
            dp[nums[0]] = True 
        
        for i in range(1, len(nums)):
            nextDp = dp[:]
            for j in range(1, target + 1):
                notTake = dp[j]
                take = dp[j - nums[i]] if nums[i] <= j else False 
                nextDp[j] = notTake or take 
            dp = nextDp 

        return dp[target]
        #1D space Optimization approach using TC-O(N * Target), SC-(Target)

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False 
        return self.func(nums, total // 2)