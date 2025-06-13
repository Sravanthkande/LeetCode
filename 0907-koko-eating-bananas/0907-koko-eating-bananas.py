class Solution:
    def cal(self, piles, mid):
        totalTime = 0
        for pile in piles:
            totalTime += math.ceil(pile / mid)
        return totalTime
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            totalTime = self.cal(piles, mid)
            if totalTime <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left