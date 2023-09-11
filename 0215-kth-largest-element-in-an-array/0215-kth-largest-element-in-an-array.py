class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      neg_nums = [-num for num in nums]
      heapq.heapify(neg_nums)

      while k > 1:
        heapq.heappop(neg_nums)
        k -= 1

      return -1 * heapq.heappop(neg_nums)