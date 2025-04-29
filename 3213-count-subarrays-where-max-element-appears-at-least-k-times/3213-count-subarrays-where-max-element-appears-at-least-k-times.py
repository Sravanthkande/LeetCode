class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        res = l = count = 0

        for r in range(len(nums)):
            if nums[r] == max_element:
                count += 1
            while count == k:
                if nums[l] == max_element:
                    count -= 1
                l += 1
            res += l
        return res