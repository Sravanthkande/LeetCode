class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key=lambda x:x[1])
        lastEnd = intervals[0][1]
        count = 1

        for i in range(1,N):
            if intervals[i][0] >= lastEnd:
                count += 1
                lastEnd = intervals[i][1]
        return N - count