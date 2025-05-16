class Solution:
    def isPossible(self, nums, day, m,k):
        count, noOfBouquets = 0, 0
        for i in range(len(nums)):
            if nums[i] <= day:
                count += 1
            else:
                noOfBouquets += (count // k)
                count = 0
        noOfBouquets += (count // k)
        return noOfBouquets >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        
        left, right = min(bloomDay), max(bloomDay)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if self.isPossible(bloomDay, mid, m, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        