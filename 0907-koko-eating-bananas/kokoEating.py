#Brute Force approach using Liner Search
import math
def minRateToEat(self, piles, h):
    maxPile = max(piles)

    for i in range(1, maxPile):
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile / i)
        
        if totalHours == h:
            return i 
    return maxPile
