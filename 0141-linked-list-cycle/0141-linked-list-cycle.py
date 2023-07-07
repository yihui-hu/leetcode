# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        """
        add node to hash map
        not value because there might be duplicates
        """

        hashMap = set()

        while (head):
          if head in hashMap:
            return True
          else:
            hashMap.add(head)
          head = head.next
        return False
          
          