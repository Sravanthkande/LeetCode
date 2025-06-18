class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
    #     if len(nums) <= 1:
    #         return []
        
    #     N = len(nums)
    #     res = []

    #     for i in range(N):
    #         for j in range(i+1, N):

    #             if nums[i] == nums[j]:
    #                 res.append(nums[i])
                
    #     return res
    #THIS IS BRUTE FROCE APPROACH USING TC-O(N^2) AND SC-O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return []
        res = []
        mapp = defaultdict(int)

        for num in nums:
            mapp[num] += 1

        for num, count in mapp.items():
            if count >= 2:
                res.append(num)
            
        return res
        #THIS IS THE OPTIMAL APPROACH USING HASHMAP TC-O(N) AND SC-O(1)
    