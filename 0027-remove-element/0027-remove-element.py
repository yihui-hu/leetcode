class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      index = 0

      for num in nums:
        # since the rest of the array doesn't matter,
        # we can just overwrite it like so
        if num != val:
          nums[index] = num
          index += 1

      """
      [3, 2, 2, 3] val = 3
      [2, 2, 2, 3] and index ends up at 2
      """
      
      return index