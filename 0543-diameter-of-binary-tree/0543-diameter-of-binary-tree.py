# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

      """
      break problem down into subproblems
      find diameter of each node starting from bottom up

      how to find diameter of curr node?
      we want both the diameter and height of its children

      height = take 1 + max(left_node_height, right_node_height)
      diameter = left_node_height + right_node_height + 2
      """

      res = [0]

      def dfs(root):
        if not root:
          return -1 # i.e. return the height of tree, which is -1 for null

        # find height of left and right subtrees
        left = dfs(root.left)
        right = dfs(root.right)

        # update diameter if greater than current result 
        res[0] = max(res[0], 2 + left + right) 

        # return height of tree
        return 1 + max(left, right) 

      dfs(root)
      return res[0]
