import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pq = []

        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        adjLs = [[] for _ in range(n + 1)] #TAKES TIME O(E)

        for u, v, wt in times:
            adjLs[u].append((v, wt))
            

        heapq.heappush(pq, (0, k))

        while pq:
            dis, node = heapq.heappop(pq) #TAKES YOU TIME O(LOG N) IN THE WORST CASE IT WILL TAKE O(E LOG N)

            for neighbour, w in adjLs[node]:

                if dist[node] + w < dist[neighbour]:
                    dist[neighbour] = dist[node] + w 
                    heapq.heappush(pq, (dist[neighbour], neighbour))
                
        maxTime = max(dist[1:])
        return maxTime if maxTime != float('inf') else -1
        #TOTAL TIME COMPLEXITY - O((N + E) LOG N)
        #SPACE COMPLEXITY - O(N + E)
        