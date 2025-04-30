class Solution:
    def numberOfSubarray(self, nums: List[int], k:int) -> int:
        #Edge Case
        if k < 0:
            return 0
        N = len(nums)
        l,r =0, 0 #Initialize two pointers
        sum_val = 0
        count = 0

        while r < N:
            sum_val += nums[r] % 2

            while sum_val > k:
                sum_val -= nums[l] % 2
                l += 1
            count += (r - l + 1)
            r += 1
        return count
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numberOfSubarray(nums, k) - self.numberOfSubarray(nums, k-1)