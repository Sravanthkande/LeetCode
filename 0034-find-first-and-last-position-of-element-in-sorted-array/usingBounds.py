class Solution:
    def lowerBound(self, nums, x):
        left , right = 0, len(nums) - 1
        ans = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= x:
                ans = mid 
                right = mid - 1
            else:
                left = mid + 1
        return ans 
    
    def upperBound(self, nums, x):
        left, right = 0, len(nums) - 1
        ans = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > x:
                ans = mid 
                right = mid - 1
            else:
                left = mid  + 1
        return ans 
    
    def firstAndLast(self, nums, x):
        first = self.lowerBound(nums, x)

        # Check if the target is present in the array or not
        if first == len(nums) or nums[first] != x:
            return [-1, -1]
        
        last = self.upperBound(nums, x) - 1
        return [first, last]