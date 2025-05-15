import math

class Solution:
    #Helper function to return sum of nums with divisor
    def getSum(self, nums, d):
        sum = 0
        for num in nums:
            sum += math.ceil(num / d)
        return sum

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        N = len(nums)
        #Edge Case
        if N > threshold:
            return -1
        
        left, right =1, max(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.getSum(nums, mid) <= threshold:
                right = mid - 1
            else:
                left = mid + 1
        return left