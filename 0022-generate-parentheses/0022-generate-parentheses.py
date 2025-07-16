class Solution:
    def generate(self, openCount, closeCount, N, curr, ans):
        if openCount == closeCount == N:
            ans.append(curr)
            return 
        
        if openCount < N:
            self.generate(openCount + 1, closeCount, N, curr + '(', ans)
        
        if closeCount < openCount:
            self.generate(openCount, closeCount + 1, N, curr + ')', ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate(0, 0, n, "",ans)
        return ans