import heapq
import copy

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        item = None
        self.nums.append(val)
        nums_heap = [-i for i in self.nums]
        for _ in range(self.k):
            heapq.heapify(nums_heap)
            item = heapq.heappop(nums_heap)
        
        return -item
