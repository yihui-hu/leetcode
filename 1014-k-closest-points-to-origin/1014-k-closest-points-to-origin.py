class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        high level understanding: we want to use a minHeap
        what do we store in a minHeap? a tuple (distance, coords)
        we sort the minheap on distance, and when we retrieve them,
        we concat the coords in the tuple into an array to return it
        """

        minHeap = []
        
        for coords in points:
          # we don't need to calculate sqrt
          dist = (coords[0] - 0) ** 2 + (coords[1] - 0) ** 2
          minHeap.append((dist, coords))
        
        heapq.heapify(minHeap)

        res = []
        for i in range(k):
          tup = heapq.heappop(minHeap)
          res.append(tup[1])

        return res