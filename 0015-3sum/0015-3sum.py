class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()

        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = N - 1

            while j < k:
                sumVal = nums[i] + nums[j] + nums[k]
                if sumVal < 0:
                    j += 1
                elif sumVal > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    res.append(temp)

                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            
        return res
        