class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        pref = strs[0]
        prefLen = len(pref)
        for s in strs[1:]:
            while pref != s[0:prefLen]:
                prefLen -= 1
                pref = pref[0:prefLen]
            
        return pref
        