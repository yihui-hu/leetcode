class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        """
        use DFS to recursively fill image
        edge cases:
        1. pixel is already new color
        2. pixel is only color of its kind
        assumptions:
        1. uniform image (set number of rows and columns, rectangular is ok)
        """

        # if image is already the new color, return
        if image[sr][sc] == color:
          return image
        
        # call fill function
        # image[sr][sc] represents current / prevColor in recursive calls
        self.fill(image, sr, sc, color, image[sr][sc])

        # return filled image
        return image

    # recursive function for filling
    # base case: out of bounds pixel or not same color
    def fill(self, image, sr, sc, color, prevColor):
      if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != prevColor:
        return
      else:
        # change pixel to new color
        image[sr][sc] = color

        # recursive call on neighbouring pixels
        self.fill(image, sr-1, sc, color, prevColor)
        self.fill(image, sr, sc-1, color, prevColor)
        self.fill(image, sr+1, sc, color, prevColor)
        self.fill(image, sr, sc+1, color, prevColor)
