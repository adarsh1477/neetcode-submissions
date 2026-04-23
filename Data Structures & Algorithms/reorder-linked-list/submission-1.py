# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return None

        slow=head
        fast=head.next

        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        if fast.next:
            slow=slow.next

        second = slow.next
        slow.next=None

        curr=second
        prev=None

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        second=prev
        first=head
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second = temp2