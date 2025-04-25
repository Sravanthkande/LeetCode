class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        leftSum , rightSum, maxSum = 0, 0, 0
        for i in range(k):
            leftSum += cardPoints[i]
            maxSum = leftSum
        right = len(cardPoints) -1
        for i in range(k -1, -1, -1):
            leftSum -= cardPoints[i]
            rightSum += cardPoints[right]
            right -= 1
            maxSum = max(maxSum, leftSum + rightSum)
        return maxSum
        