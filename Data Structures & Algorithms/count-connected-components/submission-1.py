from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        visited = set()
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def count(node):
            if node in visited: return
            visited.add(node)

            for nei in adj[node]:
                count(nei)


        for edge in range(n):
            if edge not in visited:
                count(edge)
                components += 1

        
        return components

