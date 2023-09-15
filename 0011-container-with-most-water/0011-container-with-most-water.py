class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        start with left and right pointers
        compute max area
        move pointer with smaller height
        """

        left = 0
        right = len(height) - 1

        maxVol = 0
        while left < right:
          currVol = (right - left) * min(height[left], height[right])
          maxVol = max(maxVol, currVol)
          if height[left] < height[right]:
            left += 1
          else:
            right -= 1
        
        return maxVol