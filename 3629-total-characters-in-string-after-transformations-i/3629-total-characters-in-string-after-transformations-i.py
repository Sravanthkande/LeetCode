class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for i in range(t):
            nxt = [0] * 26 
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % MOD 
            for j in range(2,26):
                nxt[j] = cnt[j-1]
            cnt = nxt 
        ans = sum(cnt) % MOD 
        return ans