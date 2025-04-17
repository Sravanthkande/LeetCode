class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        count = 0
        for i in range(N):
            for j in range(i+1,N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
        