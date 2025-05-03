def towSum(self, nums, target):
    indexed_nums = [(num, idx) for idx, num in enumerate(nums)] 
    indexed_nums.sort()
    left, right = 0, len(nums) -1
    while left < right:
        curSum = indexed_nums[left][0] + indexed_nums[right][0]
        if curSum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif curSum < target:
            left += 1
        else:
            right -= 1
    return []
