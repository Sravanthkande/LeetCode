class Solution:
    # for i in range(len(nums)):
    #         for j in range(i, len(nums)):
    #             if nums[i] > nums[j]:
    #                 nums[i], nums[j] = nums[j], nums[i]
            
    #     return nums, Brute force approach using TC-O(N) and SC-O(N)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        #optimal approach using TC-O(N) and SC-O(N)