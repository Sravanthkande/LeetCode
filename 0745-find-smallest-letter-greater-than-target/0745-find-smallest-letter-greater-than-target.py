class Solution:
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     for s in letters:
    #         if ord(s) > ord(target):
    #             return s 
    #     return letters[0] 
    # THIS THE BRUTE FORCE APPROACH USING TC-O(N) AND SC-O(1)
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            
        return letters[left] if left < len(letters) else letters[0]
        #THIS IS THE OPTIMAL APPRAOCH USING BINARY SEARCH TC-O(LOG N) AND SC-O(1)