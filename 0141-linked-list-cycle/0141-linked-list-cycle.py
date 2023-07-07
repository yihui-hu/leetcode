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

        # hashMap = set()

        # while (head):
        #   if head in hashMap:
        #     return True
        #   else:
        #     hashMap.add(head)
        #   head = head.next
        # return False

        """
        more optimized version,
        doesn't require O(n) space
        https://www.youtube.com/watch?v=gBTe7lFR3vc
        """

        slow, fast = head, head

        # we need to check both fast and fast.next
        # that they're not null since we're moving
        # the fast pointer by 2
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
          if slow == fast:
            return True
        return False
          



          
          