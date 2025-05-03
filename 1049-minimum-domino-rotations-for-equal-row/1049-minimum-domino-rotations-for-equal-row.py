from collections import Counter
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) != len(bottoms):
            return -1
        same, count1, count2 = Counter(), Counter(tops), Counter(bottoms)
        for a, b in zip(tops, bottoms):
            if a == b:
                same[a] += 1
        for i in range(1, 7):
            if count1[i] + count2[i] - same[i] == len(tops):
                return min(count1[i], count2[i]) - same[i]
        return -1
