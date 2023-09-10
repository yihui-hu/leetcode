# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        from collections import deque

        res = []
        q = deque([root])
        
        while q:
          rightSide = None 
          qLen = len(q) # at this current loop, all elems in q is one level

          for i in range(qLen):
            node = q.popleft()
            if node:
              # by the end of the for loop, rightSide will be rightmost node
              rightSide = node

              # add children to stack
              q.append(node.left)
              q.append(node.right)
          
          if rightSide:
            res.append(rightSide.val)
        
        return res
            
        