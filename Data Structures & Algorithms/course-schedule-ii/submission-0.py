class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited,visiting = set(),set()
        adj = defaultdict(list)
        result= []


        for u,v in prerequisites:
            adj[v].append(u)


        def dfs(node):
            if node in visited: return False
            visiting.add(node)

            for nei in adj[node]:
                if nei in visiting: return True
                if dfs(nei): return True

            visited.add(node)
            result.append(node)
            visiting.remove(node)
            return False








        for course in range(numCourses):
            if dfs(course): return []
        return result[::-1]