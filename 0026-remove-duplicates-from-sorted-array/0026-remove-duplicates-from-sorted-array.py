class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                temp.append(nums[i])
            i += 1

        temp.append(nums[-1])

        for j in range(len(temp)):
            nums[j] = temp[j]
        
        return len(temp)