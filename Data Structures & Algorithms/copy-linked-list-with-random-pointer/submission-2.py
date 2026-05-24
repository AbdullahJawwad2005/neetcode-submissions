"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a deep copy
        # while loop to make another node with same val and next
        # make it have the same random which is tricky because you don't 
        # have the same location and that hasn't been made yet
        # so each time its made, make an entry to the hashtable
        # one address of original, one value of node
        # (1) but what if there's a repeat (2) and what if its already passed (3) what if its the same
        # 3 -> 7 -> 4 -> 5 -> null
        # 1 -> 2 -> 3 -> null
        # what if theres a previous and future tables then?
        # ones which record past, and others which see future

        if not head:
            return None
        
        temp = head
        head2 = Node(head.val)
        temp2 = head2
        dictionary = {temp:temp2}

        while temp.next != None:
            temp = temp.next # shift to next node
            tempnxt = Node(temp.val) # make the next deep copy node
            temp2.next = tempnxt # assign that node as the next from prev
            temp2 = tempnxt
            dictionary[temp] = temp2
        
        temp2.next = None # final end
        dictionary[None] = None

        # okay now made a copy of the entire list
        # now you need another pass and go through the things together
        # the dict should have original traced to deep copy
        # needs to access keys of the rand and see the values of the copy
        temp = head
        temp2 = head2
        while temp != None:
            temp2.random = dictionary[temp.random]
            temp2 = temp2.next
            temp = temp.next
        
        return head2




        