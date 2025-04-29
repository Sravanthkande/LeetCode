class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minLen = float('inf')
        sIndex = -1

        hash = [0] * 256
        for c in t:
            hash[ord(c)] += 1
        
        count = 0
        l, r =0, 0
        while r < len(s):
            if hash[ord(s[r])] > 0:
                count += 1
            hash[ord(s[r])] -= 1

            while count ==  len(t):
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l

                hash[ord(s[l])] += 1
                if hash[ord(s[l])] > 0:
                    count -= 1
                l += 1
            r += 1
        return s[sIndex:sIndex + minLen] if sIndex != -1 else ""
        