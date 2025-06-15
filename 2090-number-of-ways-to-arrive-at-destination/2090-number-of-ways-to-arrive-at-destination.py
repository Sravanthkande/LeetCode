import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7

        adj = defaultdict(list)

        for an in roads:
            adj[an[0]].append((an[1], an[2]))
            adj[an[1]].append((an[0], an[2]))

        minTime = [float('inf')] * n

        ways = [0] * n 

        pq = []

        minTime[0] = 0
        ways[0] = 1

        heapq.heappush(pq, (0, 0))

        while pq:
            time, node = heapq.heappop(pq)

            for adjNode, travelTime in adj[node]:

                if minTime[adjNode] > time + travelTime:
                    minTime[adjNode] = time + travelTime
                    ways[adjNode] = ways[node]
                    heapq.heappush(pq, (minTime[adjNode], adjNode))

                elif minTime[adjNode] == time + travelTime:

                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod 
        return ways[n-1] % mod

        