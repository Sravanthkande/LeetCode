class Solution(object):
    def lower_bound(self, nums,value):
        left, right = 0, len(nums) -1
        res= 0
        while left <= right:
            sum = nums[left] + nums[right]
            if sum < value:
                res += right - left
                left += 1
            else:
                right -= 1
        return res
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        return self.lower_bound(nums, upper+1) - self.lower_bound(nums, lower)