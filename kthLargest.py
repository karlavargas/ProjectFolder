import heapq
class KthLargest:
    def __init__(self, k, nums):

        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)
        
        while self.k < len(self.min_heap):
            heapq.heappop(self.min_heap)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        if self.k < len(self.min_heap):
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
    
    
a = KthLargest(3, [4, 5, 8, 2]);
print(a.add(3))
