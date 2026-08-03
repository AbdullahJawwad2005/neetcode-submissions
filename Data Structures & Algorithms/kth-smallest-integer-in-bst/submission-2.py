# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # traverse it inorder then get it when the counter is large enough

        # more efficient way? because the issue here is that the runtime is severe

        cnt = 0
        res = None
        def traverse(n):
            nonlocal cnt
            nonlocal res


            if n is None or res is not None:
                return

            traverse(n.left)

            if res is not None:
                return



            cnt += 1
            if cnt == k:
                res = n.val


            traverse(n.right)
        
        traverse(root)
        return res

        