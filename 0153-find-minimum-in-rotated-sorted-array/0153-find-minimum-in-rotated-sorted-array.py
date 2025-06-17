class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     minEle = float('inf')

    #     for num in nums:
    #         if num < minEle:
    #             minEle = min(minEle, num)
            
    #     return minEle this is the brute force approach using TC-O(N) and SC-O(1)
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        
        left, right = 0, N -1 

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid 
            else:
                left = mid + 1
            

        return nums[left]
        #this is the optimal appraoch using binary search TC-O(logn) and SC-O(1)