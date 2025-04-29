class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen, maxFreq = 0, 0
        l,r = 0, 0
        hash = [0] * 26
        while r < len(s):
            hash[ord(s[r]) - ord('A')] += 1
            maxFreq = max(maxFreq, hash[ord(s[r]) - ord('A')])
            if (r - l + 1) - maxFreq > k:
                hash[ord(s[l]) - ord('A')] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen