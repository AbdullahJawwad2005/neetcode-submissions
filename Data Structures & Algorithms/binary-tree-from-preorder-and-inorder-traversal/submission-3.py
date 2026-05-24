# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) # goes from little to higher
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        















        # INORDER
        # basically take inorder array and is left -> root -> right
        # PREORDER
        # root -> left -> right
        # okay what the actual fuck you have two arrays for reference and now to solve you need to...
        # use basically both of them and combine
        # okay lets see the pattern here, you'd take elements 1-3 for the preorder one here
        # but you don't know for sure if left and right both exist or its branching one direction instead
        # is the fact that the smallest ones go on the left something that can help
        # how about using inorder to iterate and arrange then?

        if not inorder and not preorder:
            return
        self.root = TreeNode(val=0, left=None, right=None)

        # divide into two based on root and then build them separately
        # YOU BASICALLY KEEP SUBDIVIDING IN HALF I SEE IT NOW AND ADD AS YOU GO

        inorder_dict = {}
        for i in range(0, len(inorder)):
            inorder_dict[inorder[i]] = i
        
        def check(inorder, preorder, root):
            if not inorder:
                return
            temp = preorder.pop(0)
            i = inorder_dict[temp]
            left_point = inorder[:i]
            right_point = preorder[i:]
            print(left_point)
            print(right_point)
            inorder.pop(temp)
            self.root = TreeNode(val=temp, )
            check(left_point, preorder, root.left)
            check(right_point, preorder, root.right)
        check(inorder, preorder, self.root)
        return self.root





        