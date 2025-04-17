class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {} #stores array elements in hashmap
        for i in range(len(nums)):
            diff = target - nums[i] #stores the difference of nums[i] and target
            if diff in seen: #check the difference in map if found return i and map[diff]
                return [i, seen[diff]]
            seen[nums[i]] = i  # if not update nums[i] value as i in map
        return [] #return none


        
