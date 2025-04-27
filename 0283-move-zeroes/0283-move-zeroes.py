class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        forZero, forNum = 0, 0

        while forNum < N:
            if nums[forNum] != 0:
                if forNum > forZero:
                    nums[forZero], nums[forNum] = nums[forNum], nums[forZero]
                forZero += 1
            forNum += 1
        return nums
