# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # okay we use breadth first search for this
        # what basically happens is that add stuff to a global queue as you go on
        # you can add the vals to the list in order, but how do you make the sublists and tracking the levels?
        # add a tracking constant integer
        # oh okay no you can just pop one at a time
        if not root:
            return []
        queue = [root]
        output = []

        def traverse():
            if not queue:
                return
            n = len(queue)
            
            temp_list = []
            for i in range(0, n):
                # iterate and put into queue and output
                # get first node out of start and append its things and add it to the other list
                temp = queue.pop(0)
                if temp.left != None:
                    queue.append(temp.left)
                if temp.right != None:
                    queue.append(temp.right)
                temp_list.append(temp.val)
            output.append(temp_list)
            return traverse()
        traverse()
        return output

        # how do you stop the thing at ends where its ending? simple check
        #
        #
        #

        