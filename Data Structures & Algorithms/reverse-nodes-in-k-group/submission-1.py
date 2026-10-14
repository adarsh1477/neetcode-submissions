# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        operations = length//k

        def reverse(node,k):
            prev = None
            curr = node

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return curr,prev

        

        dummy = ListNode(None)
        result = dummy
        curr = head
        for  _ in range(operations):
            c,p = reverse(curr,k)
            result.next = p
            result = curr
            curr = c
        if curr:
            result.next = curr
        return dummy.next

        