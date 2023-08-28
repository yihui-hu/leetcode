# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
      """
      naive approach that takes one pass but also
      uses O(n) space

      length = 0
      nodes = []

      current = head
      while current:
        nodes.append(current)
        length += 1
        current = current.next

      middle = length // 2
      return nodes[middle]
      """

      # cool trick here

      """
      we have two pointers: one 'fast' and one 'slow'
      the fast pointer will take two 'steps' while the slow takes one
      by the time the fast pointer reaches the end, the slow pointer
      is at the middle of the linked list
      """

      slow = fast = head

      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
      return slow