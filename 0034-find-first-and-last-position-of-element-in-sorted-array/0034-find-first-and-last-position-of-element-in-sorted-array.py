class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        N = len(nums)

        for i in range(N):
            if nums[i] == target:
                if first == -1:
                    first = i 
                last = i 
        return [first, last]
        