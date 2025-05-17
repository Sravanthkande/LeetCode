class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqMap = {}
        oddFreq = 0
        for char in s:
            freqMap[char] = freqMap.get(char, 0) + 1

            if freqMap[char] % 2 == 1:
                oddFreq += 1
            else:
                oddFreq -= 1
        if oddFreq > 0:
            return len(s) - oddFreq + 1
        return len(s)
