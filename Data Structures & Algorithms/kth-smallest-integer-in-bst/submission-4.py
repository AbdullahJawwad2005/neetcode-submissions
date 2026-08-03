# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        res = None

        def traverse(node):
            nonlocal cnt
            nonlocal res

            if node is None or res is not None:
                return

            traverse(node.left)

            # The left traversal may have found the answer
            if res is not None:
                return

            cnt += 1

            if cnt == k:
                res = node.val
                return

            traverse(node.right)

        traverse(root)
        return res

        