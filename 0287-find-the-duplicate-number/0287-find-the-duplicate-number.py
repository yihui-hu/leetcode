class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      """
      this is a linked list cycle problem 
      and we have to use floyd's cycle finding algorithm
      """

      slow = fast = 0

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
