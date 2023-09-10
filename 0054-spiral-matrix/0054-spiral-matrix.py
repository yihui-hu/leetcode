class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        """
        notice that everytime we traverse across a row or column,
        we reduce the size of the matrix

        think of it like so
             L     R
             |     |
        T -> 1 2 3 4
             5 6 7 8 
        B -> 9 1 2 3

        and when we move from 1, 2, 3, 4
        it becomes this:

             L     R
             |     |
             x x x x
        T -> 5 6 7 8 
        B -> 9 1 2 3

        essentially we reduced  the size
        of the matrix by moving T down

        we move right, down, left and up (one cycle)

        this is O(m * n) time complexity and O(1)
        """

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # keep recursing while pointers are NOT crossing each other
        while left < right and top < bottom:
          # moving right
          for i in range(left, right):
            res.append(matrix[top][i])
          top += 1

          # moving down
          for i in range(top, bottom):
            res.append(matrix[i][right - 1])
          right -= 1

          # we check here for one column or row edge case
          if not (left < right and top < bottom):
            break

          # moving left
          for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
          bottom -= 1

          # moving up
          for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
          left += 1

        return res
        