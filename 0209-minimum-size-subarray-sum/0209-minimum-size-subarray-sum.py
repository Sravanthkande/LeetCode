class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, 0
        sum = 0
        res = float('inf')

        for right in range(0, len(nums)):
            sum += nums[right]

            while sum >= target:
                res = min(res, right-left+1)
                sum -= nums[left]
                left += 1

        return res if res != float('inf') else 0

        