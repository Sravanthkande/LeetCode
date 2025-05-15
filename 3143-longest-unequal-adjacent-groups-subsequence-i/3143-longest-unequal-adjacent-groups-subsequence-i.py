class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        for i in range(len(groups)-1):
            if groups[i] != groups[i+1]:
                res.append(words[i])
        res.append(words[-1])
        return res