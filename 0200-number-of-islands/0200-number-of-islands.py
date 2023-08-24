class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      # return 0 islands if grid is empty
      if not grid:
        return 0

      # get rows and cols
      ROWS, COLS = len(grid), len(grid[0])

      # initialize islands count
      islands = 0

      def bfs(r, c):
        q = collections.deque()
        q.append((r, c))

        while q:
          row, col = q.popleft()
          # set grid[r][c] to be "0" to mark as visited
          grid[row][col] = "0"
          directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
          for dr, dc in directions:
            newRow = row + dr
            newCol = col + dc
            if newRow in range(ROWS) and newCol in range(COLS) and grid[newRow][newCol] == "1":
              grid[newRow][newCol] = 0
              q.append((newRow, newCol))

      # iterate through each cell in the grid and perform BFS
      for r in range(ROWS):
        for c in range(COLS):
          if grid[r][c] == "1":
            # perform BFS on cell
            bfs(r, c)
            islands += 1
      
      return islands
