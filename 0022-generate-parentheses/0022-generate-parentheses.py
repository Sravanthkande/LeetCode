class Solution:
    def generate(self, openCount, closeCount, N, cur, ans):
        if openCount == closeCount == N:
            ans.append(cur)
            return  
        
        if openCount < N:
            self.generate(openCount + 1, closeCount, N, cur + '(', ans)
        
        if closeCount < openCount:
            self.generate(openCount, closeCount + 1, N, cur + ')', ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0, 0, n, "", ans)
        return ans