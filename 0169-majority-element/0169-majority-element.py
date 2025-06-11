class Solution:
    #Brute Force approach using HashMap TC-O(n) and SC-O(n)
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = defaultdict(int)
    #     candidate, maxCount = 0, 0

    #     for num in nums:
    #         count[num] += 1
    #         if maxCount < count[num]:
    #             candidate = num
    #             maxCount = count[num]
    #     return candidate
    def majorityElement(self, nums: List[int]) -> int:
        #Optimal Approach Using Moore Vooting Algo TC-O(n) and SC-O(1)
        count, candidate = 0, None

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        
        if nums.count(candidate) > len(nums) // 2:
            return candidate
        return None
        