class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     for i in range(len(nums)):
    #         if nums[i] == target:
    #             return i 
    #     return -1 TC-O(N) sc- O(1) using Linear Search

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1 #This is binary search using O(log n) and O(1)