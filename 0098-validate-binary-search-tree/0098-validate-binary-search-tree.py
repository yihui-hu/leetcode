# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

      """
      intuition: perform DFS
      check from bottom up if they're valid BSTs
      """

      """
      THIS SOLUTION DOES NOT WORK

      [5, 4, 6, null, null, 3, 7]

             5
            / \
           4   6
              / \
             3   7

      Note that they're all valid subtrees but since 3 is to the right
      of 5, this should return False, but the soln returns True.

      Need to do better...

      def dfs(root):
        # base case: node has no children
        if not root:
          return True

        # recurse on left and right children
        left = dfs(root.left)
        right = dfs(root.right)
        
        if left and right:
          leftValid, rightValid = False, False
          if not root.left or (root.left and root.left.val < root.val):
            leftValid = True
          if not root.right or (root.right and root.right.val > root.val):
            rightValid = True
          return leftValid and rightValid
        else:
          return False

      return dfs(root)
      """

      # # define boundaries via left and right
      # def valid(node, left, right):
      #   if not node:
      #     return True
        
      #   if not (node.val < right and node.val > left):
      #     return False
        
      #   # have to check the following cond: left < node.left < node.val
      #   return valid(node.left, left, node.val) and valid(node.right, node.val, right)
      
      # # -infinity < root < infinity, since the root can be any value
      # return valid(root, float("-inf"), float("inf"))

      def check_valid(node, leftBound, rightBound):
        if not node:
          return True
        
        if not (node.val < rightBound and node.val > leftBound):
          return False
        
        valid_left_subtree = check_valid(node.left, leftBound, node.val)
        valid_right_subtree = check_valid(node.right, node.val, rightBound)
        return valid_left_subtree and valid_right_subtree
      
      return check_valid(root, float("-inf"), float("inf"))