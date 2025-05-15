class Solution:
    def binarySearch(self, nums, target):
        left , right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        for i in range(N):
            if matrix[i][0] <= target <= matrix[i][M - 1]:
                return self.binarySearch(matrix[i], target)
        return False