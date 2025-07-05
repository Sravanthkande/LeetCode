class Solution(object):
    # def threeSum(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res = set()
    #     N = len(nums)
    #     nums.sort()

    #     for i in range(N):
    #         for j in range(i + 1, N):
    #             for k in range(j + 1, N):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     temp = [nums[i], nums[j], nums[k]]
    #                     res.add(tuple(temp))
                    
    #     return [list(i) for i in res]
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = []

        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, N - 1

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                   
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                    
        return res