class Solution:

    #Brute Force approach
    def floorandCeil(self, nums, target):
        floor, ceil = -1, -1
        

        for num in nums:
            #Floor is a number which is largest in the array and less than or equal to target
            if num <= target and num > floor:
                floor = num
            #Ceil is a number which is smallest in the array and greater than or equal to target
            if num >= target and (ceil == -1 or num < ceil):
                ceil = num 
            
        return [floor, ceil]
    def findFloor(self, nums, x):
        N = len(nums)
        left, right = 0, N - 1
        floor = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= x:
                floor = mid
                left = mid + 1
            else:
                right = mid - 1
        return floor
    def findCeil(self, nums, x):
        N = len(nums)
        left, right = 0, N-1
        ceil = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= x:
                ceil = mid
                right = mid - 1
            else:
                left =  mid + 1
        return ceil
    def optimal(self, nums, target):
        N = len(nums)

        floor = self.findFloor(nums, target)
        ceil = self.findCeil(nums, target)
        
        return [floor, ceil]
