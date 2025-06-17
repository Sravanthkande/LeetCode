class Solution:
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     peakEle = float('-inf')
    #     ind = -1

    #     for i in range(len(arr)):
    #         if arr[i] > peakEle:
    #             peakEle = max(peakEle, arr[i])
    #             ind = i
            
    #     return ind this is the brute force approach using TC - O(n) and Sc-O(1)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid 
            
        return left 
        #this is the optimal appraoch using Binary Search TC-O(log n) and SC-O(1)