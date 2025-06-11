class Solution:
    #Brute Force Solution TC - O(m * n logn) and SC - (m * n)
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         sortedS = ''.join(sorted(s))
    #         res[sortedS].append(s)
    #     return list(res.values())
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        #Optimal Approach using TC - O(m * n) and SC - O(m * n)