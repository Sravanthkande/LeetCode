class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     nums.sort()
    #     N = len(nums)

    #     closeSum = float('inf')

    #     for i in range(N):
    #         for j in range(i + 1,  N):
    #             curSum = 0
    #             for k in range(j + 1, N):
    #                 curSum = nums[i] + nums[j] + nums[k]

    #                 if abs(curSum - target) < abs(closeSum - target):
    #                     closeSum = curSum
                    
    #     return closeSum 
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        closeSum = float('inf')

        for i in range(N -2):
            l = i + 1
            r = N - 1

            curSum = 0
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if abs(curSum - target) < abs(closeSum - target):
                    closeSum = curSum 
                elif curSum < target:
                    l += 1
                else:
                    r -= 1
                
        return closeSum