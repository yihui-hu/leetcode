# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
      """
      height balanced means that subtrees must have height difference 
      no greater than 1
      use DFS
      """

      def dfs(node):

        # recurse all the way down
        # check its children first (get height of children)
        # compare height of children, if greater than 1 return False
        # current node, assign the max height of its two children

        if not node:
          return [True, 0]
        
        left = dfs(node.left)
        right = dfs(node.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        return [balanced, max(left[1], right[1]) + 1]

      return dfs(root)[0]