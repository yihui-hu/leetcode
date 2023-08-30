# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      """
      DFS
      """
      if root is None:
          return None
      if root.val == p.val or root.val == q.val:
          return root

      # if both left and right return a valid node,
      # then that means this current node is the LCA
      left = self.lowestCommonAncestor(root.left, p, q)
      right = self.lowestCommonAncestor(root.right, p, q)
      
      if left is not None and right is not None:
          return root
      
      # by the time we reach back to the root node,
      # either left or right will be NULL and have the node
      return left or right