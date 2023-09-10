class MedianFinder:

    # commented out code is okay but times out
    # see: https://www.youtube.com/watch?v=itmhHWaHupI

    """
    central idea: we don't care about the rest of the vals,
    we only care about the middle two or one

    so, we use two heaps to separate the array:
    one that contains lesser half of array (small healp),
    one that contains greater half of array (large heap)
    
    so when we want to find median, we get the max val from small heap
    and min val from large heap (or just one if heaps combined length is odd)
    """
    def __init__(self):
        # self.vals = []
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # self.vals.append(num)
        # self.vals.sort()
        heapq.heappush(self.small, -1 * num) # to make it a max heap, we multiply num by -1

        # now, make sure that every num in small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
          val = -1 * heapq.heappop(self.small)
          heapq.heappush(self.large, val)
        
        # uneven size of stack
        if len(self.small) > len(self.large) + 1:
          val = -1 * heapq.heappop(self.small)
          heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
          val = heapq.heappop(self.large)
          heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # val_len = len(self.vals)
        # if val_len % 2 == 0:
        #   right_i = val_len // 2
        #   left_i = right_i - 1
        #   return ((self.vals[left_i] + self.vals[right_i]) / 2)
        # else:
        #   i = (val_len // 2)
        #   return self.vals[i]
        if len(self.small) > len(self.large):
          return -1 * self.small[0]
        if len(self.large) > len(self.small):
          return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()