class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     N = len(intervals)
    #     visited = [False] * N
    #     res = []

    #     for i in range(N):
    #         if visited[i]:
    #             continue
    #         start, end = intervals[i]
    #         visited[i] = True 

    #         for j in range(i+1, N):
    #             if visited[j]:
    #                 continue
                
    #             a, b = intervals[j]

    #             if not (end < a or start > b):
    #                 start = min(start, a)
    #                 end = max(end, b)
    #                 visited[j] = True 
                
    #         res.append([start, end])
        
    #     return res this is the Brute force approach using TC-O(n^2) and SC-O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
            
        return res
        #This is the optimal approach TC-O(nlogn) and SC-O(n)

        