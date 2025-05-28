class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.pq = []

        for num in nums:
            if len(self.pq) < self.K:
                heapq.heappush(self.pq, num)
            
            elif num > self.pq[0]:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, num)
            
    def add(self, val: int) -> int:
        if len(self.pq) < self.K:
            heapq.heappush(self.pq, val)
            return self.pq[0]
        
        if val > self.pq[0]:
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val)
        return self.pq[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)