# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      length = 0
      nodes = []

      current = head
      while current:
        nodes.append(current)
        length += 1
        current = current.next

      middle = length // 2
      return nodes[middle]