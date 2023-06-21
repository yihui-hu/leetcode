# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        """
        1. two finger algorithm
        2. have dummy node to deal with empty list edge case
        3. compare values at each finger
        4. edge case: one list might be longer / have leftover nodes
           just append to the rest of the list
        """

        head = ListNode()
        end = head

        # while there are still items in list1 and list2
        while list1 and list2:
            # if val at l1 < val at l2
            if list1.val < list2.val:
              # put l1 into new dummy list
              end.next = list1
              # move pointer to next item in l1
              list1 = list1.next
            # same logic for inverse condition
            else:
              end.next = list2
              list2 = list2.next
            end = end.next
        
        # check for non-null lists, append to rest of the list
        if list1:
          end.next = list1
        elif list2:
          end.next = list2
        
        return head.next
