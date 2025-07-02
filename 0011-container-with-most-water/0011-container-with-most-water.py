class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     res = 0

    #     for i in range(len(height)):
    #         for j in range(i + 1, len(height)):
    #             res = max(res, min(height[i], height[j]) * (j - i))
            
    #     return res TC-O(n^2) and SC-O(1)
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height) -1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
        #TC-O(n) and SC-O(1)