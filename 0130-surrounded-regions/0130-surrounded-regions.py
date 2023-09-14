class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(r, c):
          if r not in range(ROWS) or c not in range(COLS) or board[r][c] != "O":
            return
          
          board[r][c] = "Y"
          for dr, dc in directions:
            dfs(r + dr, c + dc)

        # 1. capture unsurrounded regions using DFS on bordering cells
        for r in range(ROWS):
          for c in range(COLS):
            if (board[r][c] == "O" and 
            (r in [0, ROWS - 1] or c in [0, COLS - 1])):
              dfs(r, c)

        # 2. capture surrounded regions
        # 3. uncapture unsurrounded regions
        for r in range(ROWS):
          for c in range(COLS):
            if (board[r][c] == "O"):
              board[r][c] = "X"
            elif (board[r][c] == "Y"):
              board[r][c] = "O"
        
        return board
        