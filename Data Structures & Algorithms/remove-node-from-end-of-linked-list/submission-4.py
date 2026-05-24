# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy
        counter = 0
        while counter != n:
            first = first.next
            counter = counter + 1
       
        while first.next != None:
            first = first.next
            second = second.next
        

        second.next = second.next.next

  
        return dummy.next

        

        # 1->2->3->4->5
        # 
        