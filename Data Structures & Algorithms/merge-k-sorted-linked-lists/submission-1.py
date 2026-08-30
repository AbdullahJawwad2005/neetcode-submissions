class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        if not lists:
            return None

        def merge_lists(list1, list2):
            dummy = ListNode()
            current = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            current.next = list1 if list1 else list2

            return dummy.next

        result = lists

        while len(result) > 1:
            merged = []

            for i in range(0, len(result), 2):
                list1 = result[i]
                list2 = result[i + 1] if i + 1 < len(result) else None

                merged.append(merge_lists(list1, list2))

            result = merged

        return result[0]