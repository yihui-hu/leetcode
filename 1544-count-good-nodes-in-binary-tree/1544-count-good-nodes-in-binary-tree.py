# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        perform DFS
        for each DFS traversal, maintain max seen
        """

        self.good = 0

        def dfs(curr, max_val):
          if curr:
            if curr.val >= max_val:
              self.good += 1
            new_max = max(max_val, curr.val)
            dfs(curr.left, new_max)
            dfs(curr.right, new_max)
          return

        dfs(root, root.val)
        return self.good