from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        connected = 0
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def dfs(node):
            if node in visited: return 
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)







        for node in range(n):
            if node not in visited:
                dfs(node)
                connected +=1


        return connected