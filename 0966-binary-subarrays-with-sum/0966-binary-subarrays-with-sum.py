class Solution:
    def numSubarraysWithSumEqual(self, nums: List[int], goal: int) -> int:
        #Edge Case
        if goal < 0:
            return 0
        
        N = len(nums)
        #Intitialize two pointers
        l, r = 0, 0
        sum_val, count = 0, 0

        while r < N:
            sum_val += nums[r]

            while sum_val > goal: #at any moment sum exceeds goal
                sum_val -= nums[l] #subtract left val from sum
                l += 1 #shrink left by one place
            count += (r - l + 1)
            r += 1
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.numSubarraysWithSumEqual(nums, goal) - self.numSubarraysWithSumEqual(nums, goal -1)