class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

      """
      perform multi-source BFS on the rotten oranges
      and we also keep track of fresh oranges

      when the queue we use for BFS is empty, we know all rotten
      oranges have finished 'infecting' other oranges; if there
      are still fresh oranges, we return -1

      each time we pop from the queue, we add 1 unit of time
      """

      q = deque()
      time, fresh = 0, 0

      ROWS, COLS = len(grid), len(grid[0])
      # iterate over entire grid to find all oranges
      for r in range(ROWS):
        for c in range(COLS):
          if grid[r][c] == 1:
            fresh += 1
          elif grid[r][c] == 2:
            q.append([r, c])
      
      # perform multi source BFS
      while q and fresh > 0:
        # pop all elems off queue and perform BFS on all of them
        for _ in range(len(q)):
          r, c = q.popleft()
          # get top
          if r > 0:
            if grid[r - 1][c] == 1:
              grid[r - 1][c] = 2
              q.append([r - 1, c])
              fresh -= 1
          # get bottom
          if r < ROWS - 1:
            if grid[r + 1][c] == 1:
              grid[r + 1][c] = 2
              q.append([r + 1, c])
              fresh -= 1
          # get left
          if c > 0:
            if grid[r][c - 1] == 1:
              grid[r][c - 1] = 2
              q.append([r, c - 1])
              fresh -= 1
          # get right
          if c < COLS - 1:
            if grid[r][c + 1] == 1: 
              grid[r][c + 1] = 2
              q.append([r, c + 1])
              fresh -= 1
        time += 1

      print(fresh)

      return time if fresh == 0 else -1