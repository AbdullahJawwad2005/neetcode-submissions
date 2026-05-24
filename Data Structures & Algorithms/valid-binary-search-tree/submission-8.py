# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # how to do this, just iterate and check if the node is left < middle < right fulfilled and if its not return false
        # okay no we need a global node what do we do here
        # we need to iterate down. basically root, low, high

        def check(root, low, high):
            if root is None:
                return True

            if low < root.val < high:
                return check(root.left, low, root.val) and check(root.right, root.val, high)
            
            return False
            
        return check(root, -1001, 1001)
        