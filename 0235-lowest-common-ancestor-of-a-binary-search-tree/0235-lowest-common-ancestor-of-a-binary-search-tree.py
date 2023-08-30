# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      """
      if the two values are both greater than or less than current node,
      we can move to the right or left subtree respectively

      if they're on different sides, then we know that the current node
      is the LCA

      if one of them is the curr node, then that node is the LCA
      """

      curr = root

      while curr:
        if p.val > curr.val and q.val > curr.val:
          curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
          curr = curr.left
        else:
          return curr
