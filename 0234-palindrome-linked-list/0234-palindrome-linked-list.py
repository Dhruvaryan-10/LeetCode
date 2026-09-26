class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next 
            second = second.next
        return True 