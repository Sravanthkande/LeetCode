class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     start, end = newInterval
    #     res = []

    #     inserted = False 

    #     for s, e  in intervals:

    #         if start > e:
    #             res.append([s, e])
    #         elif end < s:

    #             if not inserted:
    #                 res.append([start, end])
    #                 inserted = True
    #             res.append([s, e])

    #         else:
    #             start = min(start, s)
    #             end = max(end, e)
    #     if not inserted:
    #         res.append([start, end])
        
    #     return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = []
        start, end = newInterval
        i = 0

        while i < N and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        while i < N and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        while i < N:
            res.append(intervals[i])
            i += 1

        return res
        