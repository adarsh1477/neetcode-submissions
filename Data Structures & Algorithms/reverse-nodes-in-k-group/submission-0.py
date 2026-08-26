# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        curr = head
        length = 0

        while curr:
            length+=1
            curr=curr.next

        size = length//k

        def reverse(node,k):
            curr = node
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return curr,prev
        

        dummy = ListNode(None)
        start = dummy
        curr = head
        for _ in range(size):
            c,p = reverse(curr,k)
            start.next = p
            start = curr
            curr = c

        if curr:
            start.next = curr

        return dummy.next

        