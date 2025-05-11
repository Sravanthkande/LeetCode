class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        left, right = 0, N-1
        mini = float('inf')

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                mini = min(mini, nums[left])
                left = mid + 1
            else:
                mini = min(mini, nums[mid])
                right = mid - 1
        return mini
        