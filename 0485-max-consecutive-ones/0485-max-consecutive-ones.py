class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, maxCount = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0
        return maxCount
        