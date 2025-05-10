class Solution:
    def lowerBound(self, nums, x):
        N = len(nums)
        left, right = 0, N-1
        ans = N

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans