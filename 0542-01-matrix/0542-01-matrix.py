class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        highly recommended (re: necessary) explainer
        https://www.youtube.com/watch?v=edXdVwkYHF8
        """

        """
        intuition: iterate over each cell
        then perform BFS on neighbouring cells
        instead of finding 1 -> 0, we find 0 -> 1 so that we don't
        have (m x n)^2 time complexity
        if we do 0 -> 1 and use BFS, we can iteratively add the
        number of steps between 0 and 1
        """ 

        """
        we maintain three data structures:
        1. original matrix
        2. visited set (for BFS traversal, so we don't revisit cells)
        3. queue that stores cells for us to perform BFS on

        if we don't want to modify the original array, we can
        keep a distance matrix and in our queue, we append
        not only the coordinates of the cell, but also the distance to
        the nearest 0.

        so in the first for loops, we would do q.append((i, j, 0)) or
        something. then subsequently as we perform BFS we would
        add to that 0
        """

        from collections import deque

        n = len(mat)
        m = len(mat[0])

        # to store cells that we want to perform BFS on
        q = deque()

        # to store visited cells
        visited = set()

        # initialize our visited set and queue with cells containing 0
        for i in range(n):
          for j in range(m):
            if mat[i][j] == 0:
              visited.add((i, j))
              q.append((i, j))

        # while queue is not empty
        while q:
            # we pop off the cell and perform BFS on it
            x, y = q.popleft()
            # for each up, down, left and right cell,
            for dirs in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
              newX, newY = x + dirs[0], y + dirs[1]
              # check that newX and newY are in bounds and not visited already
              if 0 <= newX < n and 0 <= newY < m and (newX, newY) not in visited:
                # we modify the original array to now store distances
                mat[newX][newY] = mat[x][y] + 1
                # add cell to visited set
                visited.add((newX, newY))
                # add cell to queue to visit its neighbours on next iteration
                q.append((newX, newY))

        return mat


      