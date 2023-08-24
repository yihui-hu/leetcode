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

           1
         /   \
        2     3
       / \
      4   5
    
      with this solution, we start from the bottom

      4 has a height of 0 (1 + max(left, right), where left, right = -1)
      5 has a height of 0 (same as above)
      2 has a height of 1
      etc. etc.

      we update the diameter by taking left subtree height, right st height,
      and add 2 because of the edges that connect them

      so for 4, it has diameter of -1 + -1 + 2 = 0, same for 5
      and for 2, it has diameter of 0 + 0 + 2, which we can see is true

      at any point during the recursion, we update the max diameter 
      we've seen so far 
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
