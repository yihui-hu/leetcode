class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        time = 0
        queue = collections.deque()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        # first keep track of fresh oranges and add rotten ones to queue
        for r in range(ROWS):
          for c in range(COLS):
            if grid[r][c] == 2:
              queue.append((r, c))
            elif grid[r][c] == 1:
              fresh += 1

        # while queue has rotten AND fresh > 0 (need to break out of loop)
        # for each 'level' of the queue we pop off and turn surrounding 
        # oranges rotten, decrementing fresh, adding new rotten o's to queue
        # and at each level we increment time
        while queue and fresh > 0:
          for _ in range(len(queue)):
            row, col = queue.popleft()
            for dr, dc in directions:
              new_row = row + dr
              new_col = col + dc

              if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2
                queue.append((new_row, new_col))
                fresh -= 1
          time += 1

        return time if fresh == 0 else -1

          
        