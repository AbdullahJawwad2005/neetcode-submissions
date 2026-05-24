# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        store1 = [root]
        temp1 = root
        while temp1.val != p.val:
            if temp1.val > p.val:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
            store1.append(temp1)
        store1.append(temp1)

        store2 = {root}
        temp2 = root
        while temp2.val != q.val:
            if temp2.val > q.val:
                temp2 = temp2.left
            else:
                temp2 = temp2.right
            store2.add(temp2)
        store2.add(temp2)

        for i in range(len(store1)-1, -1, -1):
            if store1[i] in store2:
                return store1[i]