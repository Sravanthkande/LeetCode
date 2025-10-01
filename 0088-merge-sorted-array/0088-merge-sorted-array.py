class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     # Step 1: Copy elements from nums2 to the end of nums1
    #     # The elements of nums1 from index m to m+n-1 are initially 0s
    #     for i in range(n):
    #         nums1[m + i] = nums2[i]

    #     # Step 2: Sort the entire nums1 array
    #     nums1.sort()
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0] * (m + n)

        left, right, i = 0, 0, 0

        while left < m and right < n:
            if nums1[left] < nums2[right]:
                res[i] = nums1[left]
                left += 1
            else:
                res[i] = nums2[right]
                right += 1
            i += 1
        
        while left < m:
            res[i] = nums1[left]
            left += 1
            i += 1
        
        while right < n:
            res[i] = nums2[right]
            right += 1
            i += 1
        
        for i in range(m+n):
            nums1[i] = res[i]