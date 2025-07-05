class Solution:
    def __init__(self):
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def func(self, digits, ans, index, cur):
        if index == len(digits):
            ans.append(cur)
            return 
        
        s = self.map[int(digits[index])]

        for char in s:
            self.func(digits, ans, index + 1, cur + char)

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res 
        
        self.func(digits, res, 0, "")
        return res 