class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = [(i,x) for i,x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i,x), (j,y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:
                for k in range(i+1, j):
                    cmp_value = (k-i > j-k) - (k-i < j-k)
                    ans[k] = '.LR'[cmp_value]
        return "".join(ans)