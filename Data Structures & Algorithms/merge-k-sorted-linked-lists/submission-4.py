# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        heap = []

        for i,lst in enumerate(lists):
            if lst:
                heapq.heappush(heap,(lst.val,i,lst))

        dummy = ListNode(None)
        curr = dummy

        while heap:
            val,idx,node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next))


        return dummy.next
            