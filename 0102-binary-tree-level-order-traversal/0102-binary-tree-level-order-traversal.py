# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        """
        basically BFS,
        need queue to add nodes and their children when we pop them off
        """
        
        res = []
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            row = []
            for i in range(qLen):
                curr = q.popleft() # do NOT use pop
                # rmb to check that curr is NOT null, could be for root
                if (curr):
                    row.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            if row: # ensures we're not adding empty levels
                res.append(row)
            
        
        return res
        
            