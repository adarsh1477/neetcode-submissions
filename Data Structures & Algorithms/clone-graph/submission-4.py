"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:  return None
        start = node
        store = {}

        def dfs(node):
            if node not in store:
                store[node] = Node(node.val)
                for nei in node.neighbors:
                    dfs(nei)
            

        dfs(start)

        for old,new in store.items():
            for nei in old.neighbors:
                new.neighbors.append(store[nei])

        return store[start]