class Solution:
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        M = len(matrix[0])

        #Traverse through each row
        for i in range(N):

            """ Check if target is 
            present in the current row"""
            flag = self.binarySearch(matrix[i], target)

            if flag:
                return True
        return False
                    