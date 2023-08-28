class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      """
      this is a linked list cycle problem 
      and we have to use floyd's cycle finding algorithm
      """

      slow = fast = 0

      """
      because the elements are within the range of [1, n],
      we can treat the array as a representation of a linked list

      e.g.
      [0, 1, 2, 3, 4]
      [1, 3, 4, 2, 2]

      0 -> 3 -> 2 -> 4
                  <-
      
      cycle with 2 and 4

      first phase:
      advance slow and fast pointers until they intersect

      second phase:
      create second slow pointer
      advance both slow pointers until they intersect
      see proof here: https://www.youtube.com/watch?v=wjYnzkAhcNk
      but tldw; where they intersect is the index / val of the repeated num
      """

      while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
          break
      
      slow2 = 0

      while slow2 != slow:
        slow2 = nums[slow2]
        slow = nums[slow]
        if slow == slow2:
          break
      
      return slow
