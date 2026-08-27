from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)


        def cycle(node,parent):
            if node in visited: return False
            visited.add(node)                                                                                
        
            for nei in adj[node]:
                if nei in visited and nei!=parent:
                    return True
                if cycle(nei,node): return True


            return False



        if not cycle(0,-1) and len(visited) == n: return True
        return False