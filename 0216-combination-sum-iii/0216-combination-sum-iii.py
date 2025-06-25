class Solution:
    def func(self, target, start, path, k, ans):
        if target == 0 and len(path) == k:
            ans.append(list(path))
            return 
        
        if target <= 0 or len(path) > k:
            return 
        
        for i in range(start, 10):
            if i <= target:
                path.append(i)
                self.func(target - i, i + 1, path, k, ans)
                path.pop()
            else:
                break 
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.func(n, 1, [], k, ans)
        return ans
        