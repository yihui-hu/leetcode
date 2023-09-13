class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        similar to finding number of islands, but now just keeping track of island size
        we want our bfs call to return the size of island
        """

        if not grid:
          return 0
        
        ROWS, COLS = len(grid), len(grid[0])

        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def bfs(r, c):
          q = collections.deque()
          q.append((r, c))

          island_size = 1
          while q:
            row, col = q.popleft()
            grid[row][col] = 0
            
            for dr, dc in neighbors:
              new_row = row + dr
              new_col = col + dc
              if new_row in range(ROWS) and new_col in range(COLS) and grid[new_row][new_col] == 1:
                island_size += 1
                grid[new_row][new_col] = 0
                q.append((new_row, new_col))
          
          print(island_size)
          return island_size

        maxSize = 0
        for r in range(ROWS):
          for c in range(COLS):
            if grid[r][c] == 1:
              maxSize = max(maxSize, bfs(r, c))
        
        return maxSize
