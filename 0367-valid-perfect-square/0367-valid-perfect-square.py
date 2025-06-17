import math

class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     if num == 1:
    #         return True 
        
    #     for i in range(1, num):
    #         if i * i == num:
    #             return True 
        
    #     return False this is a brute force appraoch using tc-o(n) take too much time for large numbers
    # def isPerfectSquare(self, num: int) -> bool:
    #     return math.sqrt(num).is_integer() 
    #using built in approach
    
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == num:
                return True
            
            elif mid * mid < num:
                left = mid + 1
            
            else:
                right = mid - 1

        return False
        #THIS IS THE OPTIMAL SOLUTION FOR THIS USING BINARY SEARCH TC-O(LOG N) AND SC-O(1)