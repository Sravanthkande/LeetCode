class Solution:
    #This is the brute force approach using TC-O(n) and SC-O(n)
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     temp = []
    #     for num in nums:
    #         if num != val:
    #             temp.append(num)
        
    #     for i in range(len(temp)):
    #         nums[i] = temp[i]
    #     return len(temp)
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
        #This is the optimal approach using TC-O(n) and SC-O(1) using two pointer approach