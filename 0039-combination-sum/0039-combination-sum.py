class Solution:
    def func(self, candidates, i, target, path, ans):
        if target == 0:
            ans.append(path[:])
            return  
        
        if target < 0 or i < 0:
            return 
        
        self.func(candidates, i -1, target, path, ans)
        path.append(candidates[i])
        self.func(candidates, i, target - candidates[i], path, ans)
        path.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.func(candidates, len(candidates) -1, target, [], ans)
        return ans