from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj =[[] for _ in range(n)]

        for it in flights:
            adj[it[0]].append((it[1], it[2]))

        minDist = [float('inf')] * n 

        que = deque([(0, src, 0)])

        while que:
            stops, node, dist = que.popleft()

            if stops > k:
                continue 
            
            for adjNode, edgeWt in adj[node]:

                if(dist + edgeWt < minDist[adjNode] and
                   stops <= k):

                   minDist[adjNode] = dist + edgeWt 
                   que.append((stops + 1, adjNode, dist + edgeWt))

        if minDist[dst] == float('inf'):
            return -1
        
        return minDist[dst]