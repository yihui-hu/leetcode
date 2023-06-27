# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        """
        use recursion to traverse tree and swap children
        use DFS to visit every single node, and swap children
        edge cases:
        1. empty tree
        2. tree with only one node (i.e. only root)
        3. check if children exists
        """

        # if root is null, tree doesn't exist, simply return None
        if not root:
          return None
        
        # swap children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recurse on the left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # remember to return the (new) root!
        return root