class Solution:
    def func(self, v, i, sum, v2, ans):
        #Base Case
        if sum == 0:
            ans.append(v2[:])
            return 
        
        #Base check for negative sum or no elements left
        if sum < 0 or i < 0:
            return 
        
        #exclude the current element and start fromt the next
        self.func(v, i - 1, sum, v2, ans)

        v2.append(v[i])

        self.func(v, i, sum - v[i], v2, ans)

        v2.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        v = candidates[:]
        self.func(v, len(v) -1, target, [], ans)
        return ans