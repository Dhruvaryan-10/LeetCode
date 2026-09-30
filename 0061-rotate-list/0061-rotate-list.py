class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        k = k % length
        if k == 0:
            return head
        curr = head 
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        return new_head
        