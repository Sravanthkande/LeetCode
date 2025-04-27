class Solution(object):
    def reverseArray(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = k % N #Handle the cases where k is greater than length of the array

        self.reverseArray(nums, 0,  N-1) #reverse the entire array
        self.reverseArray(nums, 0, k-1) #reverse the first k elements
        self.reverseArray(nums, k, N-1) #reverse the remaining elements