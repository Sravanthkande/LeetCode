import math
class Solution:
    def calculateHours(self, nums, hour):
        totalHours = 0
        for num in nums:
            totalHours += math.ceil(num/ hour)
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) //2
            totalHours = self.calculateHours(piles, mid)
            if totalHours <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left