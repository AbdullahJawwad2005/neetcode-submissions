# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if (p == None and q != None) or (q==None and p!=None):
            return False
        
        comparison = True
        if p.left == None or q.left == None:
            if p.left != q.left:
                comparison = False
        else: 
            if p.left.val != q.left.val:
                comparison = False 
        
        if p.right == None or q.right == None:
            if p.right != q.right:
                comparison = False
        else: 
            if p.right.val != q.right.val:
                comparison = False 

        if p.val != q.val:
            comparison = False
        
        if comparison:
            right = self.isSameTree(p.right, q.right)
            left = self.isSameTree(p.left, q.left)
            if right and left:
                return True
            else: 
                return False
        else:
            return False


