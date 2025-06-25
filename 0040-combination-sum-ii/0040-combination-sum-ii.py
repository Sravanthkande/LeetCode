class Solution:
    def func(self, candidates, start, target, path, ans):

        if target == 0:
            ans.append(path[:])
            return 
        
        if target < 0 or start < 0:
            return 
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i -1]:
                continue 
            
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            self.func(candidates, i+1, target - candidates[i], path, ans)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.func(candidates, 0, target, [], ans)
        return ans
        