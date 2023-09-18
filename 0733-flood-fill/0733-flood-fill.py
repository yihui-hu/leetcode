class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

      """
      perform bfs
      """

      rows, cols = len(image), len(image[0])
      og_color = image[sr][sc]

      if image[sr][sc] == color:
        return image

      def bfs(r, c):
        if r not in range(rows) or c not in range(cols) or image[r][c] != og_color:
          return
        else:
          image[r][c] = color
          bfs(r + 1, c)
          bfs(r - 1, c)
          bfs(r, c + 1)
          bfs(r, c - 1)
      
      bfs(sr, sc)
      return image
        
        