# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # okay big big big issue is that we're treating the tree like binary
  
        if not root:
            return False

        def check(root_clone, subRoot_clone):
            # okay we need to make a comparison while ending it right
            if root_clone == None and subRoot_clone == None:
                return True
            if not root_clone or not subRoot_clone:
                return False

            if root_clone.val != subRoot_clone.val:
                return False

            return (check(root_clone.left, subRoot_clone.left) and check(root_clone.right, subRoot_clone.right))


        if check(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

            
        



