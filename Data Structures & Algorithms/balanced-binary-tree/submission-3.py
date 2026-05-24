# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def depth(root):
            if not root:
                return 0
            
            left_length = depth(root.left)
            right_length = depth(root.right)
            
            return 1 + max(left_length, right_length)
        
        def check(root):
            if not root:
                return True
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)
            
            if abs(left_depth - right_depth) > 1:
                return False
            
            return check(root.left) and check(root.right)
        
        return check(root)

    
    


        