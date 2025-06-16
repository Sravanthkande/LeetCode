import heapq
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)

        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))

        def dijkstra(start):
            pq = [(0, start)]
            dist = [float('inf')] * n
            dist[start] = 0

            while pq:
                dis, node = heapq.heappop(pq)
                for v, wt in graph[node]:
                    if dis + wt < dist[v]:
                        dist[v] = dis + wt
                        heapq.heappush(pq, (dist[v], v))

            return dist

        minCount = int(1e9)
        res = -1

        for i in range(n):
            distances = dijkstra(i)
            count = sum(1 for j in range(n) if i != j and distances[j] <= distanceThreshold)

            if count <= minCount:
                minCount = count
                res = i 
            
        return res