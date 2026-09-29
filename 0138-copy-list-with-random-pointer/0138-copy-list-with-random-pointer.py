class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            old_to_new[curr].next =(
                old_to_new[curr.next] if curr.next else None
            ) 
            old_to_new[curr].random =(
                old_to_new[curr.random] if curr.random else None
            )
            curr = curr.next
        return old_to_new[head]
