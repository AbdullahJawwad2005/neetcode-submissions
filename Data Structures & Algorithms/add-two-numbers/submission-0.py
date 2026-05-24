# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # okay simple enough to understand
        # first its that the reversed list digits is the number
        # the second is that you have to sum those two numbers
        # the third is that you have to convert to reversed linked list
        temp1 = l1
        temp2 = l2
        sum1 = 0
        sum2 = 0
        i = 0
        while temp1 != None or temp2 != None:
            if temp1 != None:
                sum1 = sum1 + temp1.val*(10**i)
                temp1 = temp1.next
            if temp2 != None:
                sum2 = sum2 + temp2.val*(10**i)
                temp2 = temp2.next
            i = i + 1
        
        total_sum = sum1 + sum2
        # iterate through linked list, and after each successive one times
        # by 10 raised to power i
        # then you add the two
        # then you modulus by 10 and keep on dividing by 10 until its 0
        

        i = 0
        head = ListNode(total_sum%10)
        total_sum = total_sum//10
        print(head.val)
        print(total_sum)
        temp = head
        while total_sum != 0:
            temp3 = ListNode(total_sum%10)
            total_sum = total_sum//10
            temp.next = temp3
            temp = temp3
        return head
            

        