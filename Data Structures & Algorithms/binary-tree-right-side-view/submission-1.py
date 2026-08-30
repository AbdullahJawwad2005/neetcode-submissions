# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # dfs middle -> right -> left

        def dfs(level, root):
            if root is None:
                return

            # main body
            if len(res) < level:
                res.append(root.val)


            # recursive case
            dfs(level+1, root.right)
            dfs(level+1, root.left)
        
        dfs(1, root)
        return res

        