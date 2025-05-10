class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = N
        left, right = 0, N-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans