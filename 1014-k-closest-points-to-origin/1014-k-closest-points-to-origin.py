class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        """
        intuition:
        iterate through points,
        calculate distance to origin
        add to a min-heap / priority queue
        then extract k times from min-heap
        """

        """
        for later: refresh how heapify works in theory
        """

        import heapq

        minHeap = []

        # iterate through all points
        for point in points:
          x = point[0]
          y = point[1]
          # don't need to calculate square root
          dist = (x ** 2) + (y ** 2)
          # we put distance as the first elem because
          # that's what we want to order the elems by
          minHeap.append([dist, x, y])

        # heapify minHeap array
        heapq.heapify(minHeap)
        result = []

        # now add back to result array by popping
        # elements off the heap
        for i in range(k):
          dist, x, y = heapq.heappop(minHeap)
          result.append((x, y))
        
        return result


