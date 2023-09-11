# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        basically BFS
        """

        from collections import deque

        res = []
        stack = deque([root])

        while stack:
          level = []
          for i in range(len(stack)):
            curr = stack.popleft()
            if curr:
              level.append(curr.val)
              stack.append(curr.left)
              stack.append(curr.right)
          if len(level) > 0:
            res.append(level)

        return res
