class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [] * N 
        for i in range(N):
            res.append(nums[nums[i]])
        return res
        