from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq1 = Counter(ransomNote)
        freq2 = Counter(magazine)
        for char in freq1:
            if freq1[char] > freq2[char]:
                return False
        return True