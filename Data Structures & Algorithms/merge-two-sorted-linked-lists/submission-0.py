# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # we merge them into list 1, and if list one is equal to or more than
        # we add it first, need to keep curr1 and curr2 to keep track of it
        # and if both curr1 and curr2 become None then you end it
        # 
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list2:
            tail.next = list2
        else:
            tail.next = list1
    

        return dummy.next


        # 1 -> 2 -> 4
        # 1 -> 3 -> 5
        