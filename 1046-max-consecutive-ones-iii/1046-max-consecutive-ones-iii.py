class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        left, right = 0, 0
        zeros, maxLen = 0, 0

        while right < N:
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            length = right - left + 1
            maxLen = max(maxLen, length)
            right += 1
        return maxLen