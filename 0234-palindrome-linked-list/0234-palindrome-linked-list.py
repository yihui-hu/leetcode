# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
      
      # naive solution using two stacks
      # basically making copy of one and reverse copy
      # then iterating through to check sameness
      # but runs into timeout
      # need to think of another soln

      from collections import deque

      stack1 = deque()
      stack2 = deque()

      curr = head
      while curr:
        stack1.append(curr)
        stack2.appendleft(curr)
        curr = curr.next

      for i in range(len(stack1)):
        if stack1[i].val != stack2[i].val:
          return False
      
      return True
      

