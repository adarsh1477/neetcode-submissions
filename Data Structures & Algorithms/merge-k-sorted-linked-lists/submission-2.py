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
        start = dummy

        while heap:
            value,idx,node = heapq.heappop(heap)
            start.next = node
            start = start.next

            if node.next:
                heapq.heappush(heap,(node.next.val,idx,node.next))


        

        return dummy.next