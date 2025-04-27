class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        count = 0
        for i in range(1,N-1):
            if nums[i] == (nums[i-1] + nums[i+1]) * 2:
                count += 1
        return count


        