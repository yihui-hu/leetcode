# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        """
        edge cases:
        1. one of the nodes is root or ancestor of the other
        intuition:
        lowest common ancestor is the *first* split of p and q
        i.e. since this is a binary tree, once either p or q
        ends up on either side of a node, we know that node is the LCA
        either that or the node is either p or q itself, then we know
        that node will be LCA because the other will be lower down the tree
        """

        curr = root

        # while curr not null i.e. keep traversing tree
        # lmao remember to do .val to get values
        while curr:
          # no split yet, both p and q are larger than curr node
          if p.val > curr.val and q.val > curr.val:
            curr = curr.right
          # no split yet, both p and q are smaller than curr node
          elif p.val < curr.val and q.val < curr.val:
            curr = curr.left
          # means that we've either split or we've found either p or q
          else:
            return curr
