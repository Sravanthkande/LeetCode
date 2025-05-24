class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = float('-inf'), 0

        for i in range(len(nums)):
            curSum += nums[i]

            if curSum > maxSum:
                maxSum = max(maxSum, curSum)
            
            if curSum < 0:
                curSum = 0
        return maxSum
