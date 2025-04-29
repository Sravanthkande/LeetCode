class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        mapp = {0:1}
        prefix_sum = 0

        for i in range(N):
            prefix_sum += nums[i]
            sum_to_remove = prefix_sum - k 
            count += mapp.get(sum_to_remove, 0)
            mapp[prefix_sum] = mapp.get(prefix_sum, 0) + 1
        return count