# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        d1 = head.next
        d2 = head
        while d1 and d2:
            if d1 == d2:
                return True
            d1 = d1.next
            if d1 == d2:
                return True
            if d1 == None:
                return False
            d1 = d1.next
            d2 = d2.next
        return False

        