from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        visited,visiting = set(),set()
        for u,v in prerequisites:
            adj[v].append(u)

        def dfs(node):
            if node in visited: return False
            visiting.add(node)

            for nei in adj[node]:
                if nei in visiting: return True
                if dfs(nei): return True

            visited.add(node)
            visiting.remove(node)
            return False


        
        for course in range(numCourses):
            if dfs(course): return False


        return True
            