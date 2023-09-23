class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        # i represents current index of char in word
        def dfs(r, c, i):
          # if we reached the last char, we found word
          if i == len(word):
            return True
          # if r, c out of bounds, or chat doesn't match, or seen cell alr
          if (r not in range(ROWS) or 
              c not in range(COLS) or
              board[r][c] != word[i] or
              (r, c) in path):
              return False
          
          # when we reach here, means we found valid path
          # add current cell to path
          path.add((r, c))
          result = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
          # remove current cell from path
          path.remove((r, c))
          return result
        
        # perform DFS on each cell
        # if any cell returns true after DFSing, we know there is a valid path
        for r in range(ROWS):
          for c in range(COLS):
            if dfs(r, c, 0):
              return True
        
        return False