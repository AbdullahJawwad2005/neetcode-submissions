# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None
        
        # merge two lists function
        def merge_list(list1, list2):
            new_list = ListNode()
            head = new_list
            while list1 and list2:
                if list1.val < list2.val:
                    new_list.next = ListNode(list1.val)
                    new_list = new_list.next
                    list1 = list1.next
                else:
                    new_list.next = ListNode(list2.val)
                    new_list = new_list.next
                    list2 = list2.next
            if list1 is None:
                while list2:
                    new_list.next = ListNode(list2.val)
                    new_list = new_list.next
                    list2 = list2.next
            elif list2 is None:
                while list1:
                    new_list.next = ListNode(list1.val)
                    new_list = new_list.next                        
                    list1 = list1.next
            return head.next
        
        
        res = lists
        while len(res) > 1:
            temp = []
            for i in range(0, len(res), 2):
                list1 = res[i]
                list2 = res[i+1] if (i+1)<len(res) else None
                new_list = merge_list(list1,list2)
                temp.append(new_list)
            res = temp
        return res[0]

            




        
        