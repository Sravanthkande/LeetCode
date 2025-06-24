class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if n == 1:
    #         return x
        
    #     if n  < 0:
    #         x = 1/x
    #         n = -n
    #     ans = x**n
    #     return ans this is the brute force approach using TC-O(N) and SC-O(1)
    def recursive(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        
        if (n % 2 == 0):
            return self.recursive(x*x, n//2)
        return x * self.recursive(x, n-1)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0/ self.recursive(x, -n)
        
        return self.recursive(x,n)
        #This is the optimal solution using recursion TC-O(log N) and SC-O(log N)