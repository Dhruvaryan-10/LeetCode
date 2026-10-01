class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            group_start = group_prev.next
            prev = group_next
            curr = group_start
            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            group_prev.next = kth
            group_prev = group_start
    
