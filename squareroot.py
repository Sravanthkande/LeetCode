#This is the problem to find square root of n 
class Solution:
    def squareRoot(self, n):
        ans = 0
        for i in range(1, n+1):
            val = i * i 
            if val <= n:
                ans = i 
            else:
                break 
        return ans
    n = int(input())
    print(squareRoot(n))