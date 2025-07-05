class Solution:
    def findLucky(self, arr: List[int]) -> int:
        seen = {}

        for num in arr:
            seen[num] = seen.get(num, 0) + 1
        
        lucky = -1
        for num, count in seen.items():
            if count == num:
                lucky = max(lucky, num)
            
        return lucky