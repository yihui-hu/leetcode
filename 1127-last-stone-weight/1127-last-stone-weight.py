class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-s for s in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
          x = -1 * heapq.heappop(negative_stones)
          y = -1 * heapq.heappop(negative_stones)

          if x >= y:
            new = x - y
            heapq.heappush(negative_stones, -1 * new)
          elif x <= y:
            new = y - x
            heapq.heappush(negative_stones, -1 * new)
        
        return -1 * negative_stones[0]
