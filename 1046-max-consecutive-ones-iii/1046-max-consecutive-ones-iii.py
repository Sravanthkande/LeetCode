class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left, right = 0, 0
        zeros, maxLen = 0, 0

        while right < N:
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            if zeros <= k:
                length = right - left + 1
                maxLen = max(maxLen, length)
            right += 1
        return maxLen