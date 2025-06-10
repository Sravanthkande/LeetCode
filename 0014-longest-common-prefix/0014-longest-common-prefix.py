class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        minLen = min(len(s) for s in strs)
        left, right = 0, minLen

        while left < right:
            mid = (left + right + 1) // 2
            prefix = strs[0][:mid]

            if all(s.startswith(prefix) for s in strs):
                left = mid 
            else:
                right = mid - 1
        return strs[0][:left]