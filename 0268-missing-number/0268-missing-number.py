class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        maxSum = N * (N+1) // 2
        totalSum = sum(nums)
        return maxSum - totalSum
        