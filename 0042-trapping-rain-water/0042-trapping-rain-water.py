class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        if N == 0:
            return 0
        
        total = 0
        leftMax, rightMax = height[0], height[-1]

        left, right = 0, N-1

        while left <= right:
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
        