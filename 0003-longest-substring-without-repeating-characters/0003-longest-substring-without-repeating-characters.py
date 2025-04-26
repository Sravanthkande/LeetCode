class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        maxLen = 0

        for i in range(N):
            hashset = [0] * 256
            for j in range(i ,N):
                #Check if s[j] is already in current substring window
                if hashset[ord(s[j])] == 1:
                    break
                #if not update hashset
                hashset[ord(s[j])] = 1

                #Calculate the current length
                current_len = j - i + 1
                #Update maxLen
                maxLen = max(maxLen, current_len)
        return maxLen

        