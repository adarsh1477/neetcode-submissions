"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        start = head
        store = {}


        curr = head
        while curr:
            store[curr] = Node(curr.val)
            curr = curr.next


        for old,new in store.items():
            if old.next:
                new.next = store[old.next]
            if old.random:
                new.random = store[old.random]


        return store[start]



        