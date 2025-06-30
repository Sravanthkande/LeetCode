class Solution:
    # def findPrefixMax(self, nums, N):
    #     prefixMax = [0] * N 
    #     prefixMax[0] = nums[0]
    #     for i in range(1, N):
    #         prefixMax[i] = max(prefixMax[i - 1], nums[i])
        
    #     return prefixMax
    
    # def findSuffixMax(self, nums, N):
    #     suffixMax = [0] * N
    #     suffixMax[N-1] = nums[N -1]

    #     for i in range(N -2, -1, -1):
    #         suffixMax[i] = max(suffixMax[i + 1], nums[i])
        
    #     return suffixMax

    # def trap(self, height: List[int]) -> int:
    #     N = len(height)
    #     total = 0

    #     leftMax = self.findPrefixMax(height, N)
    #     rightMax = self.findSuffixMax(height, N)

    #     for i in range(N):
    #         if(
    #             height[i] < leftMax[i] and
    #             height[i] < rightMax[i]):

    #             total += (min(leftMax[i], rightMax[i]) - height[i])
            
    #     return total this brute force approach using TC-O(N) and SC-O(N)
    def trap(self, height: List[int]) -> int:
        N = len(height)

        leftMax, rightMax = 0, 0

        left, right = 0, N -1
        total = 0

        while left < right:
            if height[left] <= height[right]:
                if leftMax > height[left]:
                    total += leftMax - height[left]
                else:
                    leftMax = height[left]
                
                left += 1
            else:
                if rightMax > height[right]:
                    total += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
            
        return total
        #This is the optimal approach using TC-O(N) and SC-O(1)