class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        left, right = 0, (N*M) -1
        #Here right is used to take the 2D array as 1D array
        #Ex: N = 3, M = 4, N*M = 12. so 12 Elements are in matrix
        #We will take matrix as a 1D array and get the coordinates
        while left <= right:
            mid = (left + right) // 2

            #Get the coordinates of the mid
            #Ex: mid // M = 5//4 = 1, mid %M = 5 % 4 = 1. the coordinate is (1,1)
            row = mid // M 
            col = mid % M 

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False