class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     N = len(nums)
    #     for i in range(N):
    #         if nums[i] >= target:
    #             return i
    #     return N tc-O(n), sc-O(1) using linear search

    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res #Using binary search tc-O(logn) and sc-O(1)

            