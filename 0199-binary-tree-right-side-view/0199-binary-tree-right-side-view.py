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

        """
        note: we can't just simply traverse right nodes, see this tree:

           1
          / \
         3   6
          \
           5

        the person will see 1, 6 AND 5

        what we need to do is perform level order traversal
        and get the rightmost node of each level
        """

        from collections import deque

        res = []
        q = deque()
        q.append(root) # or just do q = deque([root]) above
        
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
          
          # don't forget to add rightmost node of this curr loop / level to res
          if rightSide:
            res.append(rightSide.val)
        
        return res
            
        