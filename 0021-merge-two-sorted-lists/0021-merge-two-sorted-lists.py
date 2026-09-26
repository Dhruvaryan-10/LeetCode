class Solution:
    def mergeTwoLists(self,list1: Optional[ListNode],list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail  = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next
