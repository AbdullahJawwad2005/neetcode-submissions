# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # okay so basically the same but this time make sure to add a counter here
        # it should be global, and a max that the value has to be greater than to add to it
        if not root:
            return None

        self.N = 0

        def check(root, high):
            if root is None:
                return 
            
            print(root.val)
            print(root.val >= high)
            if root.val >= high:
                self.N += 1
                high = root.val
            
            check(root.left, high)
            check(root.right, high)

            return


        check(root, root.val)
        return self.N
        