"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        stk = []
        start=node
        stk.append(start)
        visited = set()
        pairs = {}
        visited.add(start)


        while stk:
            node = stk.pop()
            pairs[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)



        for old,new in pairs.items():
            for nei in old.neighbors:
                new_nei = pairs[nei]
                new.neighbors.append(new_nei)


        return pairs[start]

        








