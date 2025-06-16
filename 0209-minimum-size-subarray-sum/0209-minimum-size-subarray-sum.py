class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        Sum = 0
        res = float('inf')

        for right in range(0, len(nums)):
            Sum += nums[right]

            while Sum >= target:
                res = min(res, right - left + 1)
                Sum -= nums[left]
                left += 1
            
        return res if res != float('inf') else 0