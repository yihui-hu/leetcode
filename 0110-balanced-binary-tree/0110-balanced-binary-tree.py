# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        """
        because of the definition of height-balanced
        we want to check from the bottom up
        if we do top down it will be O(n * n)
        since we have to check height of subtrees for each node
        """

        # we need this helper function to return
        # a boolean (is it balanced or not?) and the height of the (sub)tree
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)

            # remember dfs() return [isBalanced, height]
            # so left[0], right[0] tells us if (sub)tree is balanced
            # and left[1], right[1] tells us the height(s) of the (sub)trees
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # return to parent
            return [balanced, 1 + max(left[1], right[1])]
    
        # perform dfs on the root, return first item i.e. isBalanced
        return dfs(root)[0]





        
