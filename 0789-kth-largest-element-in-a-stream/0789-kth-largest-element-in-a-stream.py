class KthLargest:
    """
    clever approach: we use a heap, but it's minimum heap
    so how do we retrieve the kth element from it?

    well, we'll always just maintain a heap size of k and heappeek from it

    let's say we have nums = [4, 5, 8, 2] and k = 3

    we pop from nums while len(nums) > k
    essentially, we want the heap size to = k
    so that we can just peek, and that value will be guaranteed to be kth largest
    """

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > k:
          heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # pop the smallest value, but check edge case of heap length < k
        if len(self.heap) > self.k:
          heapq.heappop(self.heap)

        # peek, will always be stored at 0th index
        return self.heap[0] 



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)