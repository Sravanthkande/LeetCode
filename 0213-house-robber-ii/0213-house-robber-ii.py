class Solution:
    def func(self, nums):
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, N):
            temp = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = temp
        return prev

    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        
        nums1 = nums[:-1]
        nums2 = nums[1:]

        ans1 = self.func(nums1)
        ans2 = self.func(nums2)

        return max(ans1, ans2)
        