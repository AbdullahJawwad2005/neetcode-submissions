# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
       
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # stores best for future reference
        self.best = 0

        def depth(root):
            if not root:
                return 0
            
            left_height = depth(root.left)
            right_height = depth(root.right)
            
            self.best = max(self.best, left_height + right_height)

            return 1 + max(left_height, right_height)
            # okay
        depth(root)
        return self.best



        