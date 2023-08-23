from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        # initialize queue and keep track of fresh
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r, c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # now, run through queue and perform multi source BFS
        while q and fresh > 0:
            # to perform multi source BFS, pop all items off and run BFS same time
            for _ in range(len(q)):
                r, c = q.popleft()
                for r2, c2 in directions:
                    new_r, new_c = r + r2, c + c2

                    if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        q.append([new_r, new_c])
                        fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1
