# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # okay so depth first search
        # so find the most of the left subtree and most of the right
        # then return bigger one plus 1
        # so first the end case when nothings related
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1

        # get the max depth of each of the nodes and then compare and return
        left_depth = 0
        right_depth = 0
        if root.left != None:
            left_depth = self.maxDepth(root.left)
        if root.right != None:
            right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

        
        