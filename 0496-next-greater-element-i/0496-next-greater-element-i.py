class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []

    #     for num in nums1:

    #         if num in nums2:
    #             index = nums2.index(num)
    #             nextGreater = -1
    #             for i in range(index + 1, len(nums2)):
    #                 if nums2[i] > num:
    #                     nextGreater = nums2[i]
    #                     break 
    #             res.append(nextGreater)
    #         else:
    #             res.append(-1)
            
    #     return res this is the brute force solution 
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}

        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[stack.pop()] = num 
            stack.append(num)
        
        return [nextGreater.get(num, -1) for num in nums1]
        #this is the optimal solution using monotonic stack