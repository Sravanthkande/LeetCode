class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        same, right = 0, -1
        count = Counter()
        ans = 0
        for left in range(N):
            while same < k and right+1 < N:
                right += 1
                same += count[nums[right]]
                count[nums[right]] += 1
            if same >= k:
                ans += N - right
            count[nums[left]] -= 1
            same -= count[nums[left]]
        return ans
        