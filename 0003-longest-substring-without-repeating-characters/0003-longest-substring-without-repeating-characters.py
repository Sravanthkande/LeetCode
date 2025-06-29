class Solution(object):
    # class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     def unique(sub):
    #         return len(set(sub)) == len(sub)
        
    #     maxLen = 0
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             if unique(s[i:j]):
    #                 maxLen = max(maxLen,j - i)
    #     return maxLen this is the brute force approach using tc- O(n^3) and sc -O (n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, maxLen = 0, 0
        seen = {}

        for i, char in enumerate(s):
            if char in seen and start <= seen[char]:
                start = seen[char] + 1
            else:
                maxLen = max(maxLen, i- start + 1)
            
            seen[char] = i
        return maxLen
        #Optimal approach using TC-O(N) and SC-O(min(n, m))