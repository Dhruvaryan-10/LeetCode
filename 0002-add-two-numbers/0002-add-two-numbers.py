
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail  = dummy
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2 or carry:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            tail.next = ListNode(digit)
            tail = tail.next 
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        return dummy.next
