class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()
        N = len(digits)

        for i in range(N):
            for j in range(N):
                for k in range(N):

                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        res = sorted(list(nums))
        return res